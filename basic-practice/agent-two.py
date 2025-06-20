class ChatAgent:
    def __init__(self, name="PyAgent"):
        self.name = name
        self.memory = []

    def get_intent(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return "greeting"
        elif "your name" in user_input:
            return "name_query"
        elif any(word in user_input for word in ["bye", "varata"]):
            return "farewell"
        elif "help" in user_input:
            return "help"
        elif "remember" in user_input:
            return "remember"
        elif "show memory" in user_input:
            return "show_memory"
        else:
            return "unknown"

    def respond(self, user_input):
        intent = self.get_intent(user_input)

        if intent == "greeting":
            return "Hello! How can I assist you?"
        elif intent == "name_query":
            return f"My name is {self.name}."
        elif intent == "farewell":
            return "Goodbye! Come back anytime."
        elif intent == "help":
            return "You can say things like 'hello', ask for my name, or tell me to remember something."
        elif intent == "remember":
            fact = user_input.lower().replace("remember", "").strip()
            if fact:
                self.memory.append(fact)
                return f"I'll remember that: '{fact}'"
            else:
                return "What would you like me to remember?"
        elif intent == "show_memory":
            if not self.memory:
                return "I don't remember anything yet."
            return "Here's what I remember:\n- " + "\n- ".join(self.memory)
        else:
            return "Hmm, I didn't quite catch that. Try asking something else."

    def chat(self):
        print(f"{self.name}: Hello! Type 'exit' to end.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print(f"{self.name}: Bye!")
                break
            response = self.respond(user_input)
            print(f"{self.name}:", response)


agent = ChatAgent("Neo")  # You can give your agent a name
agent.chat()
