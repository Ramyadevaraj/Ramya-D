import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")


def get_learning_recommendations(topic):
    try:
        prompt = f"""
Create a personalized learning roadmap for:

{topic}

Requirements:

1. Beginner Level
2. Intermediate Level
3. Advanced Level

For each level provide:

- Topics to learn
- Recommended resources
- Videos
- Books
- Websites
- Practice suggestions

Make it structured and easy to follow.
"""

        response = model.generate_content(prompt)

        if response and response.text:
            return response.text

        return "No learning path generated."

    except Exception as e:
        return f"Error: {str(e)}"