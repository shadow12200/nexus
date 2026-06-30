#python
#we will fetch and execute commands in this script
import subprocess
import os
#command_obj = commands()
CONTAINER = "nexus-sandbox"

def docker_exec(command):
    return subprocess.run(
        [
            "docker",
            "exec",
            CONTAINER,
            "bash",
            "-c",
            command,
        ],
        capture_output=True,
        text=True,
    )


def git_initialise(myproject):#resolved and working
    commands = [
    f"cd {myproject}",
    "git init -b main",
    "git add .",
    'git commit -m "Initial commit"',
    f"gh repo create {myproject} --private --source=. --remote=origin --push"
]
    main_cmd="\n".join(commands)
    docker_exec(main_cmd)

def git_push(pwd):
    message = input("Commit message: ")

    commands = [
        f"cd {pwd}",
        "git add .",
        f'git commit -m "{message}"',
        "git push"
    ]

    result = docker_exec("\n".join(commands))

    if result.returncode != 0:
        print(result.stderr)
    else:
        print("✓ Changes pushed successfully.")

def check_initial():
    pwd=os.getcwd()
    if pwd == "/home/blackops/nexus":
        os.chdir("nexus_sandbox")
    else:
        raise Exception("Not in the correct directory. Please run this script from /home/blackops/nexus")   
    command = "docker exec -it nexus-sandbox bash -c 'echo Hello from inside the container!'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def execute_commands(command_obj,prelist):
    language = command_obj["language"]
    commands = []
    for i in prelist : commands.append(i)
    for i in command_obj["commands"] : commands.append(i)

    if language != "bash":
        raise ValueError(f"Unsupported language: {language}")

    script = "\n".join(commands)

    result = docker_exec(script)

    print(result.stdout)

    if result.returncode != 0:
        print(f"Error executing commands")
        print(result.stderr)
        
                

def wrapped_main(command_obj,prelist):
    check_initial()
    execute_commands(command_obj,prelist)
    
