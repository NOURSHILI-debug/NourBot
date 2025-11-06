from ChatBot.bot import ChatBot
if __name__ == "__main__":
    bot=ChatBot(name="NourBot")
    print("Welcome to NourBot! Type 'exit' to quit.")


    while True:
        user_input=input("you: ")
        if user_input.lower() == "exit":
            print("NourBot: Goodbye! Have a great day!")
            break
        response=bot.get_response(user_input)
        print(f"NourBot: {response}")