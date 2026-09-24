# ===== PART 1: setup (runs once) =====
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
MODEL = "gemini-flash-lite-latest"

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)


# ===== PART 2: the function (a recipe; it doesn't run until called) =====
def ask_gemini(question):
    start = time.perf_counter()
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=question,
            # config=config,
        )
        answer = response.text
    except Exception as e:
        answer = f"ERROR: {e}"
    seconds = time.perf_counter() - start
    return answer, seconds


# ===== PART 3: use the function =====
answer, seconds = ask_gemini("What is the latest version of Python?")
answer, seconds = ask_gemini("What is the latest version of Node.js?")
print("ANSWER:", answer)
print(f"TIME: {seconds:.1f}s")

