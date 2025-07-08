from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_file import run_file
import re
import json
from messenger import Message, Messenger


def has_func_call(response, messages):
    pat = r"([{].*?[}]+)"
    func = re.search(pat, response)
    if func is not None:
        print("REGEX CHECK")
        print(func.group())
        print("REGEX END")
        try:
            func_dict = json.loads(func.group())
            print(f"Sent function: {func_dict["function"]}")
        except Exception as e:
            print(f"Error: {e}")
            error_message = Message(
                "system", f"It was not possible to serialize found JSON string {func.group()}")
        return True

    else:
        return False
