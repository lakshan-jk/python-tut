import pdfplumber 
import os

print(os.path.exists("/Users/lakshan/Documents/python-tut/basic-practice/Lakshan-Resume.pdf"))

class GenerativeResumeAgent:
    def __init__(self, pdf_path):
        self.text = self._extract_text(pdf_path)

    def _extract_text(self, pdf_path):
        try:
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
            full_text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"
            return full_text.strip()
        except Exception as e:
            print(f"❌ Error opening PDF: {e}")
            raise

    def ask(self, question):
        prompt = f"""
You are a helpful assistant analyzing a candidate's resume.
Here is the resume content:

\"\"\"
{self.text}
\"\"\"

Answer the following question based only on the resume:

Q: {question}
A:"""

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"❌ Error getting response from OpenAI: {e}"

    def chat(self):
        print("📄 Generative Resume AI Agent is ready. Type 'exit' to quit.")
        while True:
            q = input("You: ")
            if q.lower() in ["exit", "quit"]:
                print("Agent: Bye!")
                break
            response = self.ask(q)
            print("Agent:", response)

if __name__ == "__main__":
    try:
        agent = GenerativeResumeAgent("/Users/lakshan/Documents/python-tut/basic-practice/Lakshan-Resume.pdf")
        agent.chat()
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")