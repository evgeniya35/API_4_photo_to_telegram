import os
import requests
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv

from load_photo import load_photo, photo_ext


def fetch_apod(options, folder):
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url=url, params=options)
    response.raise_for_status()
    for num, photo in enumerate(response.json()):
        if photo["media_type"] == "image":
            load_photo(
                photo["url"],
                os.path.join(folder, f"nasa{num}{photo_ext(photo['url'])}")
            )


def fetch_epic(options, folder):
    url = "https://epic.gsfc.nasa.gov/api/natural"
    response = requests.get(url=url, params=options)
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
            options={"api_key": options["api_key"]}
        )


def main():
    load_dotenv()
    os.makedirs(os.path.join(os.getcwd(), "images", "nasa"), exist_ok=True)
    options = {
        "api_key": os.environ.get("NASA_API_KEY"),
        "start_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
        "end_date": datetime.now().strftime("%Y-%m-%d")
    }
    fetch_apod(options, os.path.join(os.getcwd(), "images", "nasa"))

    options = {"api_key": os.environ.get("NASA_API_KEY")}
    fetch_epic(options, os.path.join(os.getcwd(), "images", "nasa"))


if __name__ == "__main__":
    main()
