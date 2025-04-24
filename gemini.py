from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
transcript_file = client.files.upload(file="foo.txt")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Give me a 100-second summary of this podcast episode transcript.", transcript_file],
)
print(GEMINI_API_KEY)
print(response.text)