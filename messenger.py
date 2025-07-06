from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file


class Messenger():
    def __init__(self):
        self.messages = []

    def insert_message(self, message):
        if isinstance(message, Message):
            self.messages.append(message.formated())

    def get_messages(self):
        return self.messages


class Message():
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def formated(self):
        return {"role": self.role, "content": self.content}
