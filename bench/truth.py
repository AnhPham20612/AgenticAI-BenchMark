import datetime
import requests

def get_truth(product):
    """return the newest version, and other latest version of other maintained lines"""
    r = requests.get(f"https://endoflife.date/api/v1/products/{product}", timeout=30)
    release = r.json()["results"]["releases"]
    today =datetime.date.today().isoformat()
