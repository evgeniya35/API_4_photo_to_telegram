import os
import requests
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv

from load_photo import loadphoto


def fetch_epic_nasa_photo():
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
    fetch_epic_nasa_photo()


if __name__ == "__main__":
    main()
