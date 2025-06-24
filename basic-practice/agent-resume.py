
import fitz  
import re

class ResumeAgent:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.load_pdf()
        self.sections = self.extract_sections()

    def load_pdf(self):
        doc = fitz.open(self.pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def extract_sections(self):
        """
        Extract sections like EDUCATION, SKILLS, EXPERIENCE based on ALL CAPS headers.
        Returns a dict: {section_name: content}
        """
        lines = self.text.split("\n")
        section_dict = {}
        current_section = None
        buffer = []

        for line in lines:
            line_stripped = line.strip()
            if re.match(r"^[A-Z\s]{3,}$", line_stripped) and len(line_stripped) < 50:
                if current_section:
                    section_dict[current_section] = "\n".join(buffer).strip()
                    buffer = []
                current_section = line_stripped
            elif current_section:
                buffer.append(line_stripped)

        # Add the last buffered section
        if current_section and buffer:
            section_dict[current_section] = "\n".join(buffer).strip()

        return section_dict

    def get_answer(self, query):
        query = query.lower()

        if "name" in query:
            return "Name: Lakshan Kumar J"

        elif "email" in query:
            match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", self.text)
            return f"Email: {match.group()}" if match else "Email not found."

        elif "phone" in query or "mobile" in query:
            match = re.search(r"\+91[-\s]?\d{5}[-\s]?\d{5}", self.text)
            return f"Phone: {match.group()}" if match else "Phone number not found."

        elif "linkedin" in query:
            match = re.search(r"https:\/\/www\.linkedin\.com\/in\/[a-zA-Z0-9\-]+", self.text)
            return f"LinkedIn: {match.group()}" if match else "LinkedIn profile not found."

        elif "skill" in query:
            return f"Skills:\n{self.sections.get('SKILLS', 'Skills section not found.')}"

        elif "experience" in query:
            return f"Experience:\n{self.sections.get('EXPERIENCE', 'Experience section not found.')}"

        elif "education" in query:
            return f"Education:\n{self.sections.get('EDUCATION', 'Education section not found.')}"

        elif "certifica" in query:
            return f"Certifications:\n{self.sections.get('CERTIFICATIONS', 'Certifications section not found.')}"

        elif "summary" in query:
            return f"Summary:\n{self.sections.get('SUMMARY', 'Summary section not found.')}"

        else:
            return "Sorry, I don't understand that. Try asking about skills, experience, education, etc."

    def chat(self):
        print("📄 Resume AI Agent is ready. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Agent: Bye!")
                break
            response = self.get_answer(user_input)
            print("Agent:", response)


agent = ResumeAgent("/Users/lakshan/Documents/python-tut/basic-practice/Lakshan-Resume.pdf")
agent.chat()