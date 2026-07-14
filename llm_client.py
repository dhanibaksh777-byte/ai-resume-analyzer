from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("groq_api_key")
if api_key is None:
    raise RuntimeError("groq api key is missing from .env file")

client = Groq(api_key=api_key)

def ai_resume_analyzer(messages: list):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = messages
    )
    return response.choices[0].message.content




