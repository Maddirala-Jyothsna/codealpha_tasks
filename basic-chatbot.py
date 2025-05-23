def calculator():
    print("🧮 Welcome to the Basic Calculator")
    print("Operations: +  -  *  /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator.")
                continue

            print(f"Result: {result}")

            again = input("Do you want to calculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Goodbye!")
                break

        except ValueError:
            print("⚠️Please enter valid numbers.")
def chatbot():
    print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['bye', 'exit', 'quit']:
            print("ChatBot: Goodbye!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("ChatBot: Hello there! 😊")
        elif 'how are you' in user_input:
            print("ChatBot: I'm doing great! How about you?")
            while True:
                    user_input = input("You: ").lower()
                    if user_input in ['good','great']:
                         print("ChatBot: That's a good sign!")
                    elif user_input in ['sad','not sure','not happy']:
                        print("ChatBot: Do you wanna talk about it? 😀")
                    elif 'boring' in user_input:
                        print("Try watching interesting movie or series and recommend it to your friends. 😄")
                    else:
                        break
        elif 'your name' in user_input:   
            print("ChatBot: I'm ChatBot, your virtual assistant!")
        elif 'help' in user_input:
            print("ChatBot: I'm here to chat with you. Ask me anything!")
        elif 'basic calculation' in user_input:
            calculator()
        elif 'thank you' in user_input:
            print("I'm glab i could help you. 😊")
        else:
            print("ChatBot: I'm not sure how to respond to that. 🤔")

# Run the chatbot
chatbot()

