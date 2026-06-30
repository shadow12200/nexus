#python
#we will fetch and execute commands in this script
import subprocess
import os
from communicator import main as commands

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


def git_initialise(myproject):
    commands=['git init',f'gh repo create {myproject} --private --source=. --remote=origin','git add .','git commit -m "auto commit"','git push']
    main_cmd="\n".join(commands)
    docker_exec(main_cmd)


def git_push():
    commands=['git add .',f'git commit -m {input('commit message :')}','git push']
    main_cmd="\n".join(commands)
    docker_exec(main_cmd)

def check_initial():
    pwd=os.getcwd()
    if pwd == "/home/blackops/nexus":
        os.chdir("nexus_sandbox")
    else:
        raise Exception("Not in the correct directory. Please run this script from /home/blackops/nexus")   
    command = "docker exec -it nexus-sandbox bash -c 'echo Hello from inside the container!'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def execute_commands(command_obj):
    language = command_obj["language"]
    commands = command_obj["commands"]

    if language != "bash":
        raise ValueError(f"Unsupported language: {language}")

    script = "\n".join(commands)

    result = docker_exec(script)

    print(result.stdout)

    if result.returncode != 0:
        print(f"Error executing commands")
        print(result.stderr)
        
                

def wrapped_main():
    check_initial()
    command_obj = commands()
    execute_commands(command_obj)
