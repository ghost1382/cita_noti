import os
import time
from dotenv import load_dotenv
from telegram import Bot

from cita_checker import check_appointment
from keep_alive import keep_alive  # If using Flask to keep app alive

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)
keep_alive()  # Starts a Flask web server (required for uptime bots like UptimeRobot)

# 🚨 Notify on startup
bot.send_message(chat_id=CHAT_ID, text="✅ Bot started! Checking for citas...")

def notify(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

# 💡 Check every 30 seconds for test
while True:
    try:
        print("🟡 Checking for appointment...")
        if check_appointment():
            notify("🚨 ¡CITA DISPONIBLE PARA HUELLAS EN TORTOSA!")
        else:
            print("⏳ No appointment available.")
    except Exception as e:
        print("❌ Error during check:", e)

    time.sleep(30)
