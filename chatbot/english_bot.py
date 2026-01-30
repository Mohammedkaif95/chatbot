print("🤖 Hello! I am English Practice Bot.")
print("Type a sentence in English.")
print("Type 'bye' to exit.\n")

while True:
    sentence = input("You: ")

    if sentence.lower() == "bye":
        print("Bot: Goodbye! Keep practicing English 👋")
        break

    # Simple corrections
    if sentence.lower() == "i am fine":
        print("Bot: ✔ Correct sentence!")
        print("Bot: You can also say: 'I am doing well.'")

    elif sentence.lower() == "i have laptop":
        print("Bot: ❌ Small correction")
        print("Bot: ✔ 'I have a laptop.'")

    elif sentence.lower() == "i am learning python":
        print("Bot: ✔ Very good sentence! 👍")

    else:
        print("Bot: 👍 Nice sentence!")
        print("Bot: Tip: Try using full sentences with 'a', 'the', or verbs.")
