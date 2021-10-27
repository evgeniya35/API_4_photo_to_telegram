import os
import requests
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote

from load_photo import loadphoto


def photo_ext(url):
    url_components = urlparse(unquote(url, encoding="utf-8"))
    return os.path.splitext(url_components.path)[-1]


def fetch_nasa_photo(days=3):
    load_dotenv()
    options = {
        "api_key": os.environ.get("NASA_API_KEY"),
        "start_date": (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d"),
        "end_date": datetime.now().strftime("%Y-%m-%d")
    } 
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url=url, params=options)
    response.raise_for_status()
    for num, photo in enumerate(response.json()):
        if photo["media_type"] == "image":
            loadphoto(
                photo["url"],
                r"images\nasa",
                f"nasa{num}{photo_ext(photo['url'])}"
            )
    

def main():
    fetch_nasa_photo(days=4)


if __name__ == "__main__":
     main()
