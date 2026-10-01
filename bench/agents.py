import os
import json
import time

import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


# ===================== Gemini =====================
gemini_client = genai.Client()
GEMINI_MODEL = "gemini-3.6-flash"

# Google Search is turned off for now (not available on the free tier).
# To turn it on, uncomment `config=gemini_config` inside ask_gemini.
gemini_config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)


def ask_gemini(question):
    start = time.perf_counter()
    try:
        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=question,
            # config=gemini_config,
        )
        answer = response.text
    except Exception as e:
        answer = f"ERROR: {e}"
    seconds = time.perf_counter() - start
    return answer, seconds