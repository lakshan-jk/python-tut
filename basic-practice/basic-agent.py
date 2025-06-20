def basic_agent(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "your name" in user_input or "what's your name" in user_input:
        return "parthiban"
    elif "kena" in user_input:
        return "🙂"
    elif 'seri' in user_input:
        return "leo leo leo leo leooooo"
    elif "🙁" in user_input:
        return "ithulam thevaya unaku, leo pakanum leo ah pakanum"
    else:
        return "I'm sorry,Can you please rephrase your question?"


while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    RESPONSE = basic_agent(user_message)
    print("Chatbot:", RESPONSE)
