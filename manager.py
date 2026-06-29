LOGO=('''
░███    ░██    ░██████████    ░██    ░██    ░██     ░██      ░██████   
░████   ░██    ░██             ░██  ░██     ░██     ░██     ░██   ░██  
░██░██  ░██    ░██              ░██░██      ░██     ░██    ░██         
░██ ░██ ░██    ░█████████        ░███       ░██     ░██     ░████████  
░██  ░██░██    ░██              ░██░██      ░██     ░██            ░██ 
░██   ░████    ░██             ░██  ░██      ░██   ░██      ░██   ░██  
░██    ░███    ░██████████    ░██    ░██      ░██████        ░██████   
                                                                       
''')


def get_details():
    print(LOGO)
    data=[]
    if input("is this a new project? (y/n): ") == "y":
        project_name = input("Enter the project name: ")
        data.append(project_name)
    else:
        data.append(None)
    
    return data

def run_main():
    project_name = get_details()[0]
    if project_name:
        print(f"initialising project: {project_name}")
        #provide workflow to initialise dir and git
    else:
        pwd=input("please entre project directory :")
        #skip initialisation and move to implementation
