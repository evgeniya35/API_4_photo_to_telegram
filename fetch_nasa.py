import os
import requests
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv

from load_photo import loadphoto, photo_ext


def fetch_apod(days=2):
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


def fetch_epic():
    load_dotenv()
    options = {"api_key": os.environ.get("NASA_API_KEY")}
    url = "https://epic.gsfc.nasa.gov/api/natural"
    response = requests.get(url=url, params=options)
    response.raise_for_status()
    for photo in response.json():
        date_photo = datetime.strptime(photo["date"], "%Y-%m-%d %H:%M:%S")
        name_photo = photo["image"]
        url = (
            f"https://epic.gsfc.nasa.gov/archive/natural"
            f"/{date_photo.year}/{date_photo.month}/{date_photo.day}"
            f"/png/{name_photo}.png?api_key={options['api_key']}"
        )
        loadphoto(
            url,
            r"images\nasa",
            f"{name_photo}.png"
        )


def main():
    fetch_apod(days=1)
    fetch_epic()


if __name__ == "__main__":
    main()
