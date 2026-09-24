import datetime
import requests
import yaml


def get_latest_version(product):
    r = requests.get(f"https://endoflife.date/api/v1/products/{product}", timeout=30)
    data = r.json()
    releases = data["result"]["releases"]

    today = datetime.date.today().isoformat()   # e.g. "2026-09-24"

    # Walk through the release lines, newest first,
    # and return the first one that is actually out already.
    for release in releases:
        if release.get("latest") and release["releaseDate"] <= today:
            return release["latest"]["name"]

    return None   # nothing released at all (shouldn't normally happen)


# Load the questions
with open("questions.yaml", encoding="utf-8") as f:
    questions = yaml.safe_load(f)["questions"]

# Build the answer key
for q in questions:
    if q["grader"] != "version":   # skip trick questions and manual ones
        continue
    version = get_latest_version(q["product"])
    print(f"{q['id']:<12} -> {version}")