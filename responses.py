def get_bot_response(message: str) -> str:
    user_message = message.lower().strip()

    if user_message == "bye":
        return "Goodbye! Have a great day."

    elif "hello" in user_message or "hi" in user_message:
        return "Hello! How can I help you today?"

    elif "how are you" in user_message:
        return "I am doing well. Thanks for asking."

    elif "your name" in user_message:
        return "I am a simple Python chatbot."

    elif "help" in user_message:
        return "You can say hello, ask my name, ask how I am, or type bye to exit."

    elif "python" in user_message:
        return "Python is a popular programming language used for web, AI, automation, and more."

    elif "github" in user_message:
        return "GitHub is a platform where you can store and share your code."

    else:
        return "Sorry, I do not understand that yet."
