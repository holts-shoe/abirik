from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
transcript_file = client.files.upload(file="foo.txt")

def get_gemini_response(prompt: str, transcript_file) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, transcript_file],
    )
    return response.text
summary_prompt = "Give me a 100-second summary of this podcast episode transcript."
key_points_prompt = "Quote the most unique and interesting parts of the podcost episode transcript."
print(get_gemini_response(key_points_prompt,transcript_file))