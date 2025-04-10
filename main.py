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
print("📄 Checking page content for 'no hay citas'")
print(driver.page_source[:500])  # Print first 500 chars of HTML

while True:
    try:
        if check_appointment():
            notify("🚨 ¡CITA DISPONIBLE PARA HUELLAS EN TORTOSA!")
        else:
            print("⏳ No appointment available.")
    except Exception as e:
        print("❌ Error:", e)

    time.sleep(30)  # Wait 10 minutes

# 🔁
