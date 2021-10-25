import os
import requests

path_photo = "media\photo\hubble.jpeg"
filename = os.path.join(os.getcwd(), path_photo)
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
response = requests.get(url=url)
response.raise_for_status()
with open(filename, mode="wb") as file:
    file.write(response.content)

