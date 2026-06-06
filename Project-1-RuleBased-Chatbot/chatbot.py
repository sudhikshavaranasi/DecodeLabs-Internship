# Enhanced Rule-Based AI Chatbot

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm doing great ",
    "what is your name": "I'm DecodeBot.",
    "help": "I can greet you, tell time, answer simple questions.",
    "bye": "Goodbye!"
}

print("="*40)
print("DecodeBot Started")
print("Type 'exit' to stop")
print("="*40)

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "exit":
        print("Bot: Shutting down... Bye")
        break

    elif "thank" in user_input:
        print("Bot: You're welcome")

    elif "time" in user_input:
        from datetime import datetime
        current = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current)

    else:
        print("Bot:", responses.get(
            user_input,
            "Sorry, I don't understand that."
        ))
