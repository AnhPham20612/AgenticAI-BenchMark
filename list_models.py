from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()   # finds GEMINI_API_KEY automatically

for m in client.models.list():
    if "flash" in m.name:
        print(m.name)