import os
import requests

from urllib.parse import urlparse, unquote


def photo_ext(url):
    url_components = urlparse(unquote(url, encoding="utf-8"))
    return os.path.splitext(url_components.path)[-1]


def load_photo(url, file_name, params=None):
    headers = {"user-agent": "CoolTool / 0.0"}
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    with open(file_name, mode="wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    os.makedirs(os.path.join(os.getcwd(), "images"), exist_ok=True)
    file_name = os.path.join(os.getcwd(), "images", "hubble.jpeg")
    load_photo(
        url="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        file_name = file_name
        )
