import requests
import json
import time
import sys
from messenger import Message, Messenger
import system_prompt
from func_call import has_func_call


def main():
    cwd = "/home/martin/bootDev/boot_dev_Python_Asteroids"
    if len(sys.argv) > 1:
        test_response = """
Sancho Panza:
Ah, my friend, to unravel the tapestry of our working directory, we must first cast our gaze upon its contents. Let us summon a list of all files and directories within this realm.


```json
{
    "function": "get_file_content",
    "parameters": {
        "file_path": "main.py"
    }
}
```

This will reveal the structure and contents before us. Once done, I shall assist you further with any specific insights or tasks!
        """
        test_messenger = Messenger()
        test_message = Message("system", "First test message")
        test_messenger.insert_message(test_message)
        has_func_call(test_response, test_messenger, cwd)
        return
    # system_prompt = """You are a wise and patient debugging wizard named CodeMage.
    # You speak in a slightly mystical but friendly tone. You love helping developers
    # solve problems step-by-step. You use gentle encouragement and occasionally
    # reference magic/wizardry metaphors when explaining code concepts.
    # You're thorough but not verbose."""
    system_prompt_initial = f"""
    {system_prompt.role}
    {system_prompt.functions}
    {system_prompt.functions_descriptions}
    {system_prompt.function_call_instructions}
    {system_prompt.functions_call_example}
    {system_prompt.restrictions}
    """
    exit_chat = False
    init_message = Message("system", system_prompt_initial)
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
            using_function = True
            loops = 0
            while using_function == True and loops < 10:
                print(f"Lool - {loops}")
                response = requests.post("http://localhost:11434/api/chat", json={
                    "model": "phi3:3.8b", "messages": messages.get_messages(), "stream": False, })
            # Other models are:
                #   phi3:3.8b
                #   phi4:14b
                res_content = response.json()["message"]["content"]
                if has_func_call(res_content, messages, cwd) == False:
                    using_function = False
                    print("Sancho Panza:")
                    print(response.json()["message"]["content"])
                    # print(f"Test output --- \n{response.json()}\n")
                    response_message = Message("assistant", response.json()[
                                               "message"]["content"])
                    messages.insert_message(response_message)
                    end = time.time()
                    print(f"Execution speed: {end-start}s")
                else:
                    loops += 1
        else:
            exit_chat = True


main()
