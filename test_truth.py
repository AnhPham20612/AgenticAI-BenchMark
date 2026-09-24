import requests
import time

product = "python"

# GET = just read data (no body to send, unlike POST)
r = requests.get(f"https://endoflife.date/api/v1/products/{product}", timeout=30)
data = r.json()

releases = data["result"]["releases"]
newest = releases[0]

print("Newest release line:", newest["name"])
print("Latest version:     ", newest["latest"]["name"])
print("Released on:        ", newest["latest"]["date"])

def get_latest_version(product):
    start = time.perf_counter()
