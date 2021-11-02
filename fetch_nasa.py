import os
import requests
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv
from requests import api

from load_photo import load_photo, photo_ext


def fetch_apod(api_key, start_date, end_date, folder):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": api_key,
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.get(url=url, params=payload)
    response.raise_for_status()
    for num, photo in enumerate(response.json()):
        if photo["media_type"] == "image":
            load_photo(
                photo["url"],
                os.path.join(folder, f"nasa{num}{photo_ext(photo['url'])}")
            )


def fetch_epic(api_key, folder):
    url = "https://epic.gsfc.nasa.gov/api/natural"
    payload = {"api_key": api_key}
    response = requests.get(url=url, params=payload)
    response.raise_for_status()
    for photo in response.json():
        date_photo = datetime.strptime(photo["date"], "%Y-%m-%d %H:%M:%S")
        name_photo = photo["image"]
        url = (
            "https://epic.gsfc.nasa.gov/archive/natural"
            f"/{date_photo.year}/{date_photo.month}/{date_photo.day}"
            f"/png/{name_photo}.png"
        )
        load_photo(
            url,
            os.path.join(folder, f"{name_photo}.png"),
            options=payload
        )


def main():
    load_dotenv()
    os.makedirs(os.path.join(os.getcwd(), "images", "nasa"), exist_ok=True)
    fetch_apod(
        api_key=os.environ.get("NASA_API_KEY"),
        start_date=(datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d"),
        folder=os.path.join(os.getcwd(), "images", "nasa")
        )
    fetch_epic(
        api_key=os.environ.get("NASA_API_KEY"),
        folder=os.path.join(os.getcwd(), "images", "nasa")
        )


if __name__ == "__main__":
    main()
