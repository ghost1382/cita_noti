import os
import time

from dotenv import load_dotenv
from keep_alive import keep_alive
from cita_checker import check_appointment
import telegram

# Load environment variables
load_dotenv()

# Bot setup
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
CHAT_ID = str(os.getenv("CHAT_ID"))
bot = telegram.Bot(token=BOT_TOKEN)

# Start Flask server
keep_alive()

# 🚨 Test message on startup
bot.send_message(chat_id=CHAT_ID,
                 text="✅ Bot started! This is a test message.")


def notify(message):
                 bot.send_message(chat_id=CHAT_ID, text=message)


# 🔁
