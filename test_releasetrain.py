import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://releasetrain.io"

# os.getenv reads a value from .env (after load_dotenv has loaded it)
email = os.getenv("RELEASETRAIN_EMAIL")
password = os.getenv("RELEASETRAIN_PASSWORD")

# POST = send data to the server. json=... turns the dictionary into JSON for us.
r = requests.post(
    f"{BASE_URL}/api/auth/login",
    json={"email": email, "password": password},
    timeout=30,
)

print("STATUS CODE:", r.status_code)   # 200 means success

data = r.json()                          # turn the server's JSON reply into a Python dict
token = data["token"]
print("LOGGED IN! Token starts with:", token[:20], "...")

def ask_releasetrain(question):
    start = time.perf_counter()        # start the stopwatch
    answer = None                      # nothing found yet

    try:
        r = requests.post(
            f"{BASE_URL}/api/ask",
            headers={"Authorization": f"Bearer {token}"},
            json={"question": question, "config": {"preset": "auto"}},
            stream=True,
            timeout=300,
        )
        r.encoding = "utf-8"

        for line in r.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue

            event = json.loads(line[5:])

            if event.get("type") == "progress":
                print("  ...", event.get("phase"))
            elif event.get("type") == "result":
                answer = event.get("answer")      # ← save it instead of printing it
            elif event.get("type") == "error":
                answer = f"ERROR: {event}"

    except Exception as e:                        # network problem, timeout, etc.
        answer = f"ERROR: {e}"

    if answer is None:                            # the stream ended with no result
        answer = "ERROR: no answer received"

    seconds = time.perf_counter() - start         # stop the stopwatch
    return answer, seconds


# ===== PART 3: use it =====
answer, seconds = ask_releasetrain("What is the latest version of Python?")
print("ANSWER:", answer)
print(f"TIME: {seconds:.1f}s")