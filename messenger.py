class Messenger():
    def __init__(self):
        self.messages = []

    def insert_message(self, message):
        if isinstance(message, Message):
            self.messages.append(message.formated())

    def get_messages(self):
        return self.messages

    def len(self):
        return len(self.messages)


class Message():
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def formated(self):
        return {"role": self.role, "content": self.content}
