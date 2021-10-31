import os
import requests
import json

from load_photo import load_photo, create_folder


def fetch_spacex_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url=url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def main():
    photos = fetch_spacex_launch(launch_id="5eb87d46ffd86e000604b388")
    create_folder(os.path.join(os.getcwd(), "images", "spacex"))
    for photo_num, url in enumerate(photos):
        load_photo(
            url=url,
            file_name=os.path.join(os.getcwd(), "images", "spacex", f"spacex{photo_num}.jpg")
            )


if __name__ == "__main__":
    main()
