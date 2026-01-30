print("🤖 Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() == "hi":
        print("Bot: Hello! How are you?")
    
    elif user.lower() == "how are you":
        print("Bot: I am fine. Thank you!")
    
    elif user.lower() == "your name":
        print("Bot: My name is KaifBot 😄")
    
    elif user.lower() == "bye":
        print("Bot: Goodbye! See you again 👋")
        break

    else:
        print("Bot: Sorry, I don't understand.")
