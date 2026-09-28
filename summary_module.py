import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")


def summarize_text(text: str) -> str:
    try:
        prompt = f"""
        Summarize the following content.

        Requirements:
        - Keep important points
        - Easy to understand
        - Short and concise

        Content:
        {text}
        """

        response = model.generate_content(prompt)

        if response and response.text:
            return response.text

        return "No summary generated."

    except Exception as e:
        return f"Error: {str(e)}"
        