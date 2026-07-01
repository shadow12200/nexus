#python
#this file aims to manage memmory 
import datetime as dt



def write_to_file(filename, content):
    file_path = "/home/blackops/nexus/memory/{filename}.txt"
    with open(file_path, 'a') as file:
        file.write(f"{dt.datetime.now()} [ \n {content}\n ] \n")
        file.write(content + '\n')
    print(f"Content written to {file_path} successfully.")


def log_to_db(input_prompt, output_json, project_name):
    import sqlite3
    from datetime import datetime as dt

    # Connect to the SQLite database
    conn = sqlite3.connect("nexus.db")
    cursor = conn.cursor()

    # Get the current date and time
    current_datetime = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert the data into the table
    cursor.execute(f"INSERT INTO {project_name} (datetime, input_prompt, output_json) VALUES (?, ?, ?)",
                   (current_datetime, input_prompt, output_json))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Logged to database for project '{project_name}' successfully.")

