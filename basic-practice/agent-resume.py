import fitz
import re
import numpy as np

class ResumeAgent:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.load_pdf()
        self.memory = []
    
    def load_pdf(self):
        doc = fitz.open(self.pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    
    def get_response(self, query):
        query = query.lower()

        if "name" in query:
            # Get the first line as name (common in resumes)
            lines = self.text.split("\n")
            for line in lines:
                if re.search(r"[a-z]{2,}", line):  # any line with 2+ letters
                    return f"Name: {line.strip().title()}"
            return "Sorry, I couldn't find the name."
        
        elif "email" in query:
            match = re.search(r"(email || email address)\s*[:\-]?\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", self.text)
            return f"Email:{match.group(2)}" if match else "Sorry I couldn't find the email in the resume."

        elif "skills" in query:
            pattern = r"skills\s*[:\-]?\s*(.*)"
            matches = re.findall(pattern, self.text)
            if matches:
                return f"Skills: {matches[0].strip().title()}"
            else:
                idx = self.text.find("skills")
                if idx != -1:
                    return f"Skills: {self.text[idx:idx+200].strip()}"
                return "Skills section not found."
        
        elif "experience" in query:
            if "experience" in self.text:
                start = self.text.find("experience")
                snippet = self.text[start:start+200]
                return f"Experience: {snippet.strip()}"
            else:
                return "No experience section found."

        elif "education" in query:
            return "Education: " + self.extract_section("education", 400)

        else:
            return "I'm sorry, I couldn't find the information you're looking for."

    def chat(self):
        print("📄 Resume AI Agent is ready. Type 'exit' to quit")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Agent: {response}")

agent = ResumeAgent("/Users/lakshan/Documents/python-tut/basic-practice/Lakshan-Resume.pdf")
agent.chat()