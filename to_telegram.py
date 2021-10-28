import os

from dotenv import load_dotenv
import telegram


load_dotenv()
telegram_token = os.environ.get("TELEGRAM_TOKEN")
bot = telegram.Bot(token=telegram_token)
bot.send_document(
    chat_id="-1001730774444",
    document=open(file="images/hubble.jpeg", mode="rb")
    )
