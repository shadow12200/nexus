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
    if project_name:
        print(f"initialising project: {project_name}")
        commands=[f'mkdir {project_name}',f'cd {project_name}']
        command_obj=main()
        ex.wrapped_main(command_obj,commands)
        ex.git_initialise(project_name)
        #ex.git_push()#no problemo 
        #provide workflow to initialise dir and git


    else:
        pwd=input("please entre project directory :")
        commands=[f'chdir {pwd}']
        ex.docker_exec(commands)
        ex.wrapped_main()
        ex.git_push(pwd)

run_main()