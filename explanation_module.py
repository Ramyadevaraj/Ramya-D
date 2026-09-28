import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.8-flash")


def explain_concept(topic):
    try:
        prompt = f"""
Explain the following topic in simple beginner-friendly language.

Topic: {topic}

Use:
- Simple words
- Examples
- Step-by-step explanation
"""

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"