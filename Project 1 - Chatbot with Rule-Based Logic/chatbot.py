#!/usr/bin/env python3
def respond(user_input: str) -> str:
    text = user_input.lower().strip()
    if any(g in text for g in ["hello", "hi", "hey"]):
        return "Hello! How can I help you today?"
    if "your name" in text:
        return "I'm a simple chatbot."
    if "hours" in text:
        return "We operate 24/7 online."
    if "contact" in text:
        return "Email us at support@example.com."
    if text in ["bye", "exit", "quit"]:
        return "Goodbye!"
    return "I don't understand that."

def chat():
    print("Chatbot (type 'bye' to exit)")
    while True:
        user = input("You: ")
        if user.lower() in ["bye","exit","quit"]:
            print("Bot: Goodbye!")
            break
        print("Bot:", respond(user))

if __name__ == "__main__":
    chat()
