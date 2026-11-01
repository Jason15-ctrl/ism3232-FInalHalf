
## Module 10: OOP for Agents

## Concepts Practiced

| **Concept** | **What it does** |
| ----------- | ---------------- |
| Class | A template used to create objects |
| Object | An instance created from a class |
| Attribute | Stores data that belongs to an object |
| Method | A function defined inside a class |
| `__init__` | Initializes attributes when an object is created |
| `self` | Refers to the current object |
| Composition | Allows one object to use another object |
| `self.history` | Stores messages from a conversation |
| `respond()` | Records messages and returns a response |
| `choose_reply()` | Uses keyword rules to select a response |
| `OrderLookup` | Looks up order IDs and their statuses |
| `StockLookup` | Checks product inventory |
| `pytest -v` | Runs tests and displays detailed results |
| `ruff format .` | Formats Python code |
| `ruff check .` | Checks Python code for issues |

## Lab Summary

In this lab, I practiced using Python classes and objects to build chatbots. I created tools to check orders and stock, added conversation history, and used composition to connect the tools to the chatbot. I also created two chatbots that share tools but keep separate histories. For the mini-project, I made a nail salon assistant that checks service prices and directs certain requests to the front desk.

## Testing

All 15 tests passed using pytest.

## AI Use Statement

I used AI to help me navigate the lab and troubleshoot issues with the code.
