from os import environ
import requests
import json
from load_photo import loadphoto

def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches"
    id_launch = "5eb87d46ffd86e000604b388"
    response = requests.get(url=f"{url}/{id_launch}")
    response.raise_for_status()
    urls_photo = response.json()["links"]["flickr"]["original"]
    for photo_num, url in enumerate(urls_photo):
        loadphoto(
            url=url,
            folder="images",
            photo=f"spacex{photo_num}.jpg"
            )

if __name__ == "__main__":
    fetch_spacex_last_launch()