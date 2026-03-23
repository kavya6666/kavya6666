from responses import get_bot_response


def run_chatbot() -> None:
    print("Python Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_message = input("You: ").strip()

        if not user_message:
            print("Bot: Please type something.")
            continue

        bot_reply = get_bot_response(user_message)
        print(f"Bot: {bot_reply}")

        if user_message.lower().strip() == "bye":
            break


if __name__ == "__main__":
    run_chatbot()
