# my_assistant.py
# Author: Jason Nguyen

HANDOFF_WORDS = ["refund", "complaint", "cancel"]


class NailSalonAssistant:
    """A mock assistant that answers questions about nail service prices."""

    def __init__(self, name, instructions, price_tool):
        self.name = name
        self.instructions = instructions
        self.price_tool = price_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        if self.needs_human(text):
            return "Please contact the front desk for help with that."

        service = self.price_tool.find_service(text)
        if service is not None:
            price = self.price_tool.price_for(service)
            return f"A {service} costs ${price}."

        if "hello" in text:
            return f"Hello! I'm {self.name}. I can help you check nail service prices."

        return "I'm not sure about that. I can help you check service prices."

    def needs_human(self, text):
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False
