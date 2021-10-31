import os
import requests

from urllib.parse import urlparse, unquote


def photo_ext(url):
    url_components = urlparse(unquote(url, encoding="utf-8"))
    return os.path.splitext(url_components.path)[-1]


def create_folder(folder):
    os.makedirs(folder, exist_ok=True)


def load_photo(url, file_name):
    headers = {"user-agent": "CoolTool / 0.0"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    with open(file_name, mode="wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    create_folder(os.path.join(os.getcwd(), "images"))
    file_name = os.path.join(os.getcwd(), "images", "hubble.jpeg")
    load_photo(
        url="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        file_name = file_name
        )
