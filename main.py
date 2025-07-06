import requests
import json
import time
import sys
from messenger import Message, Messenger


def main():
    # system_prompt = """You are a wise and patient debugging wizard named CodeMage.
    # You speak in a slightly mystical but friendly tone. You love helping developers
    # solve problems step-by-step. You use gentle encouragement and occasionally
    # reference magic/wizardry metaphors when explaining code concepts.
    # You're thorough but not verbose."""
    cwd = "/home/martin/Documents/Prog/panza"
    system_prompt = """You are a wise and patient assistant named Sancho Panza.
    You speak like my old and much wiser friend. You love helping developers solve problems
    step-by-step. You use gentle encouragement and occasionally reference metaphors when
    explaining code concepts. You're thorough but not verbose.
    Our current working folder is predefined and you do not have to use it as parameter in function calls. 

    Available functions:
    - get_files_info: Takes parameter working_directory and directory. working_directory parameter is root from where will function list all files and directories, directory parameter is optional in case you want to list only in some subfolder.
    - get_file_content: Takes parameter working_directory and file_path. File_path parameter leads to file which contents you want to read. Function returns content of defined file up to 10000 characters.
    - 

    To call a function, respond with JSON in this oneline format:
{"function": "function_name", "parameters": [{"param1": "value1"}]}

    If no function is needed, respond normally.
    """
    exit_chat = False
    init_message = Message("system", system_prompt)
    messages = Messenger()
    messages.insert_message(init_message)
    # phi3:3.8b
    while exit_chat == False:
        print("Enter prompt:")
        prompt = input()

        start = time.time()
        user_message = Message("user", prompt)
        messages.insert_message(user_message)
        if prompt != "exit":
            response = requests.post("http://localhost:11434/api/chat", json={
                "model": "phi3:3.8b", "messages": messages.get_messages(), "stream": False, })

            print(response.json()["message"]["content"])
            print(f"Test output --- \n{response.json()}\n")
            response_message = Message("assistant", response.json()[
                                       "message"]["content"])
            messages.insert_message(response_message)
            end = time.time()
            print(f"Execution speed: {end-start}s")
        else:
            exit_chat = True


main()
