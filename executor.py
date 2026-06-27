#python
#we will fetch and execute commands in this script
import subprocess
import os
from communicator import main as commands

command_obj = commands()

def git_initialise(myproject):
    commands=['git init',f'gh repo create {myproject} --private --source=. --remote=origin','git add .','git commit -m "auto commit"','git push']
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error executing command: {command}")
            print(result.stderr)
            break


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

    if language == "bash":
        for command in commands:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(result.stdout)
            if result.returncode != 0:
                print(f"Error executing command: {command}")
                print(result.stderr)
                break
    else:
        raise Exception(f"Unsupported language: {language}")


check_initial()
execute_commands(command_obj)


