from my_assistant import NailSalonAssistant
from my_tool import ServicePriceLookup


def make_assistant():
    prices = {
        "manicure": 20,
        "pedicure": 35,
        "acrylic set": 50,
    }
    tool = ServicePriceLookup(prices)
    return NailSalonAssistant("Lily", "Help customers check prices.", tool)


def test_pedicure_price():
    assistant = make_assistant()
    assert assistant.respond("How much is a pedicure?") == "A pedicure costs $35."


def test_manicure_price():
    assistant = make_assistant()
    assert assistant.respond("What is the manicure price?") == "A manicure costs $20."


def test_refund_goes_to_front_desk():
    assistant = make_assistant()
    assert "front desk" in assistant.respond("I need a refund")


def test_unknown_question():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("What is the weather?")


def test_conversation_history():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("How much is a pedicure?")
    assert len(assistant.history) == 4
