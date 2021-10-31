import os
import requests

from urllib.parse import urlparse, unquote


def photo_ext(url):
    url_components = urlparse(unquote(url, encoding="utf-8"))
    return os.path.splitext(url_components.path)[-1]


def load_photo(url, folder, photo):
    if not os.path.exists(os.path.join(os.getcwd(), folder)):
        os.makedirs(os.path.join(os.getcwd(), folder))
    filename = os.path.join(os.getcwd(), folder, photo)
    headers = {"user-agent": "CoolTool / 0.0"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    with open(filename, mode="wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    load_photo(
        url="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        folder="images",
        photo="hubble.jpeg"
        )
