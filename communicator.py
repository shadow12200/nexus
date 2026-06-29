import requests
import json

def bash_prompter():

    SYSTEM_PROMPT = """
    You are Nexus.

    Return ONLY valid JSON.
    Never use markdown.
    Never wrap JSON in ```.

    Schema:

    {
    "language": "bash",
    "commands": [
        "command1",
        "command2"
    ]
    }
    """

    prompt = input("> ")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:8b",
            "system": SYSTEM_PROMPT,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()["response"]

    print(data)

    # Parse JSON
    obj = json.loads(data)
    print(type(obj))
    print("Language:", obj["language"])
    return obj 


def file_builder():
    SYSTEM_PROMPT = """
        You are Nexus.

        Return ONLY valid JSON.
        Never use markdown.
        Never wrap JSON in ```.

        start with 
        1.bash command to create file
        2.than echo statements to write to the file

        Schema:

        {
        "language": "bash",
        "commands": [
            "command1",
            "command2"
        ]
        }
        """
    prompt = input("file-prompt--> ")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:8b",
            "system": SYSTEM_PROMPT,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()["response"]

    print(data)

    # Parse JSON
    obj = json.loads(data)
    print(type(obj))
    print("Language:", obj["language"])
    return obj 

def main():
    while True:
        print("Select an option:")
        print("1. Bash Prompter")
        print("2. File Builder")
        print("3. Exit")

        choice = input("choice --> ")

        if choice == "1":
            obj = bash_prompter()
            return obj
        elif choice == "2":
            obj = file_builder()
            return obj
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


