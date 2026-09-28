import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")


def clean_json_block(text):
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)
    return text.strip()


def generate_quiz(topic):
    try:
        prompt = f"""
Generate exactly 3 MCQ questions about:

{topic}

Return ONLY valid JSON.

Format:

[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "Correct Answer"
  }}
]
"""

        response = model.generate_content(prompt)

        cleaned = clean_json_block(response.text)

        quiz_data = json.loads(cleaned)

        return quiz_data

    except Exception as e:
        return {
            "error": str(e)
        }