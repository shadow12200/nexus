import requests
import json

def main():

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

