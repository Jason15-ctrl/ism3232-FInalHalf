# my_main.py
# Author: Jason Nguyen

from my_assistant import NailSalonAssistant
from my_tool import ServicePriceLookup

PRICES = {
    "manicure": 20,
    "pedicure": 35,
    "acrylic set": 50,
}

price_tool = ServicePriceLookup(PRICES)

assistant = NailSalonAssistant(
    "Lily",
    "Help nail salon customers check service prices.",
    price_tool,
)

print("Welcome to the nail salon assistant!")
print("Type quit to stop.")

user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
