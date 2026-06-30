LOGO=('''
░███    ░██    ░██████████    ░██    ░██    ░██     ░██      ░██████   
░████   ░██    ░██             ░██  ░██     ░██     ░██     ░██   ░██  
░██░██  ░██    ░██              ░██░██      ░██     ░██    ░██         
░██ ░██ ░██    ░█████████        ░███       ░██     ░██     ░████████  
░██  ░██░██    ░██              ░██░██      ░██     ░██            ░██ 
░██   ░████    ░██             ░██  ░██      ░██   ░██      ░██   ░██  
░██    ░███    ░██████████    ░██    ░██      ░██████        ░██████   
                                                                       
''')

from communicator import main 
import executor as ex


def get_details():
 
    data=[]
    if input("is this a new project? (y/n): ") == "y":
        project_name = input("Enter the project name: ")
        data.append(project_name)
    else:
        data.append(None)
    
    return data

def run_main():#need to model behaviour based on initialisation condition
    print(LOGO)
    project_name = get_details()[0]
    if project_name:# this branch is working as intended 
        print(f"initialising project: {project_name}")
        commands=[f'mkdir {project_name}',f'cd {project_name}']
        command_obj=main()
        ex.wrapped_main(command_obj,commands)
        ex.git_initialise(project_name)

    else:
        pwd=input("please entre project directory :")
        commands=[f'cd {pwd}']
        command_obj=main()
        ex.wrapped_main(command_obj,commands)
        ex.git_push(pwd)

run_main()