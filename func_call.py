from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_file import run_file
import re
import json
from messenger import Message, Messenger

functions_available = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_file": run_file
}


def successful_call(messages, value):
    new_message = Message("system", f"{value}")
    messages.insert_message(new_message)


def has_func_call(response, messages, working_directory):
    pat = r"([{].*?[}]{2,})"
    response_no_new_lines = response.replace("\n", "")
    response_no_new_lines = response_no_new_lines.replace(" ", "")
    func = re.search(pat, response_no_new_lines)
    if func is not None:
        # print("REGEX CHECK")
        # print(func.group())
        # print("REGEX END")
        try:
            func_dict = json.loads(func.group())
            function = func_dict["function"]
            parameters = func_dict["parameters"]
        except Exception as e:
            error_message = Message(
                "system", f"<error>It was not possible to serialize found JSON string: {func.group()}</error><original_error_message>{e}</original_error_message>")
            messages.insert_message(error_message)
        try:
            match function:
                case "get_files_info":
                    if "directory" in parameters:
                        successful_call(messages, functions_available[function](
                            working_directory, parameters["directory"]))
                    else:
                        successful_call(
                            messages, functions_available[function](working_directory))
                case "get_file_content":
                    if "file_path" in parameters:
                        successful_call(messages, functions_available[function](
                            working_directory, parameters["file_path"]))
                    else:
                        error_message = Message(
                            "system", f"<error>Expected parameter was not found - <parameter>file_path</parameter></error>")
                        messages.insert_message(error_message)
                case "run_file":
                    if "file_path" in parameters:
                        successful_call(messages, functions_available[function](
                            working_directory, parameters["file_path"]))
                    else:
                        error_message = Message(
                            "system", f"<error>Expected parameter was not found - <parameter>file_path</parameter></error>")
                        messages.insert_message(error_message)
                case _:
                    error_message = Message(
                        "system", f"<error>Requested function is unknown</error>")
                    messages.insert_message(error_message)
            return True
        except Exception as e:
            print(f"Error: {e}")
            error_message = Message(
                "system", f"<error>It was not possible to run requested function: {func.group()}</error><original_error_message>{e}</original_error_message>")
            messages.insert_message(error_message)
    else:
        return False
