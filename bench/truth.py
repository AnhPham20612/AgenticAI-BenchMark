import datetime
import requests

def get_truth(product):
    """return the newest version, and other latest version of other maintained lines"""
    r = requests.get(f"https://endoflife.date/api/v1/products/{product}", timeout=30)
    releases = r.json()["result"]["releases"]
    today =datetime.date.today().isoformat()


    released = [rel for rel in releases
                if rel.get("latest") and rel["releaseDate"] <= today]

    newest = released[0]["latest"]["name"]

    partial = [rel["latest"]["name"] for rel in released[1:]
            if rel.get("isMaintained")]

    return newest, partial