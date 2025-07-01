import random
import re

class SmartAgent:
    def __init__(self, name="Leo"):
        self.name = name
        self.memory = []
        self.last_intent = None
        self.user_name = None

    def extract_name(self, text):
        match = re.search(r"my name is (\w+)", text, re.IGNORECASE)
        return match.group(1) if match else None

    def detect_mood(self, text):
        if any(word in text for word in ["happy", "good", "great", "awesome"]):
            return "positive"
        elif any(word in text for word in ["sad", "bad", "terrible", "horrible"]):
            return "negative"
        return None

    def get_intent(self, user_input):
        user_input = user_input.lower()

        if any(word in user_input for word in ["hello", "hi", "hey"]):
            return "greeting"
        elif any(word in user_input for word in ["bye","varata", "see you"]):
            return "farewell"
        elif "your name" in user_input:
            return "name_query"
        elif "remember" in user_input:
            return "remember"
        elif "show memory" in user_input:
            return "show_memory"
        elif "my name is" in user_input:
            return "store_name"
        elif self.detect_mood(user_input):
            return "mood"
        else:
            return "unknown"

    def respond(self, user_input):
        intent = self.get_intent(user_input)
        self.last_intent = intent

        if intent == "greeting":
            return random.choice(["Hi There!", "Hello!","Hey!, How can i help you!"])
        elif intent == "name_query":
            return f"My name is {self.name}, your helpful assistant"
        elif intent =="farewell":
            return random.choice(["Goodbye!", "See you later!", "Have a nice day!", "varata","aala vidra"])
        elif intent == "remember":
            fact = user_input.lower().replace("remember", "").strip()
            if fact:
                self.memory.append(fact)
                return f"I'll remember that: '{fact}'"
            else:
                return "What would you like me to remember?"
        elif intent == "show_memory":
            return "I remember:\n" + "\n".join(f"- {item}" for item in self.memory) if self.memory else "I don't remember anything yet."
        elif intent == "store_name":
            name = self.extract_name(user_input)
            if name: 
                self.user_name = name  # <-- Fix here
                return f"Nice to meet you, {name}!"
            return "I'm sorry,Yaara nee?."
        elif intent == "mood":
            mood = self.detect_mood(user_input)
            if mood == "negative":
                return "I'm sorry you're feeling that way. Want to talk about it?"
            elif mood == "positive":
                return "That's great!😉"
        else:
            return random.choice([
            "Hmm, I'm not sure I understand",
            "Can you say that differently",
            "I'm still learning. Could you rephrase that?"
            ])
        return fallback
    
    def chat(self):
        print(f"{self.name}: Hello! Type 'exit' to end.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print(f"{self.name}: Bye!")
                break
            response = self.respond(user_input)
            print(f"{self.name}:", response)

agent= SmartAgent("Neo")
agent.chat()