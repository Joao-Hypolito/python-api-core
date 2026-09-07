import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
if len(api_key) > 0:
    client = genai.Client(
        api_key=api_key
    )


def get_course_ai_description(name):

    prompt = """
Me mostre uma descrição do curso {} em no máximo 250 caracteres.
"""
    prompt = prompt.format(name)

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text