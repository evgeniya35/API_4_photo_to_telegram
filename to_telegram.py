import os
import time
import telegram

from dotenv import load_dotenv


def pub_image(telegram_token, telegram_channel, delay=86400):
    bot = telegram.Bot(token=telegram_token)
    while True:
        for dir_path, dir_names, file_names in os.walk("images"):
            for file_name in file_names:
                with open(file=os.path.join(dir_path, file_name), mode="rb") as f:
                    doc = f.read()
                bot.send_document(
                    chat_id=telegram_channel,
                    document=doc
                    )
                time.sleep(delay)


def main():
    load_dotenv()
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    telegram_channel = os.environ.get("TELEGRAM_CHANNEL")
    delay = int(os.environ.get("PUBLISH_DELAY"))
    pub_image(telegram_token, telegram_channel, delay)


if __name__ == "__main__":
    main()
