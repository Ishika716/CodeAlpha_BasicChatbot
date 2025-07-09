def simple_chatbot():
    """
    A simple rule-based chatbot that responds to predefined user inputs.
    """
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase

        if "hello" in user_input:
            print("Chatbot: Hi! 👋")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thanks! 😊")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! 👋 Have a great day!")
            break  # Exit the loop and end the conversation
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase? 🤔")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()