import os
import requests
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote

from requests.sessions import extract_cookies_to_jar

from load_photo import loadphoto


def fetch_spacex_last_launch(url):
    response = requests.get(url=url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


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
    
    url = "https://api.spacexdata.com/v5/launches/5eb87d46ffd86e000604b388"
    photos = fetch_spacex_last_launch(url=url)
    for photo_num, url in enumerate(photos):
        loadphoto(
            url=url,
            folder="images\spacex",
            photo=f"spacex{photo_num}.jpg"
            )


if __name__ == "__main__":
     main()

    
