import os
import time
import telegram

from dotenv import load_dotenv


def pub_image():
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    delay = int(os.environ.get("PUBLISH_DELAY", 86400))
    telegram_channel = os.environ.get("TELEGRAM_CHANNEL")
    bot = telegram.Bot(token=telegram_token)
    while True:
        for dir_path, dir_names, file_names in os.walk("images"):
            for file_name in file_names:
                bot.send_document(
                    chat_id=telegram_channel,
                    document=open(file=os.path.join(dir_path, file_name), mode="rb")
                    )
        time.sleep(delay)


if __name__ == "__main__":
    load_dotenv()
    pub_image()
