import os
import time
import telegram

from dotenv import load_dotenv


def pub_image(delay=86400):
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    bot = telegram.Bot(token=telegram_token)
    while True:
        for dpath, dirnames, fnames in os.walk("images"):
            for fname in fnames:
                bot.send_document(
                    chat_id="-1001730774444",
                    document=open(file=os.path.join(dpath, fname), mode="rb")
                    )
        time.sleep(delay)


if __name__ == "__main__":
    load_dotenv()
    delay = int(os.environ.get("PUBLISH_DELAY"))
    pub_image(delay)
