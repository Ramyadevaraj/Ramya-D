import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")


def answer_question(question: str) -> str:
    try:
        prompt = f"""
        You are EduGenie, an AI educational assistant.

        Answer the following question clearly and accurately.

        Question:
        {question}
        """

        response = model.generate_content(prompt)

        if response and response.text:
            return response.text

        return "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"