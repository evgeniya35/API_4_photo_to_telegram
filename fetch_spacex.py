import os
import requests
import json

from load_photo import load_photo


def fetch_spacex_launch(launch_id, folder):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url=url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]
    for photo_num, url in images:
        load_photo(
            url=url,
            file_name=os.path.join(folder, f"spacex{photo_num}.jpg")
            )


def main():
    os.makedirs(os.path.join(os.getcwd(), "images", "spacex"), exist_ok=True)
    fetch_spacex_launch(
        launch_id="5eb87d46ffd86e000604b388",
        folder=os.path.join(os.getcwd(), "images", "spacex")
        )


if __name__ == "__main__":
    main()
