import os
import requests

def loadphoto(url, folder, photo):
    if not os.path.exists(os.path.join(os.getcwd(), folder)):
        os.makedirs(os.path.join(os.getcwd(), folder))
    filename = os.path.join(os.getcwd(), folder, photo)
    headers = {"user-agent": "CoolTool / 0.0"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    with open(filename, mode="wb") as file:
        file.write(response.content)


if __name__ == "__main__":       
    loadphoto(
        url="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        folder="images",
        photo="hubble.jpeg"
        )
