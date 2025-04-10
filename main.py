import os
import time
from dotenv import load_dotenv
from telegram 
from cita_checker import check_appointment
from keep_alive import keep_alive

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=BOT_TOKEN)

keep_alive()

# Initial test
bot.send_message(chat_id=CHAT_ID,
                 text="✅ Bot started! This is a test message.")

print("🟡 Checking for appointment...")
if check_appointment():
                 notify("🚨 ¡CITA DISPONIBLE PARA HUELLAS EN CASTELLÓN!")
else:
                 print("⏳ No appointment available.")


def notify(message):
                 bot.send_message(chat_id=CHAT_ID, text=message)


while True:
                 try:
                                  print("🔄 Checking for appointment...")
                                  if check_appointment():
                                                   notify(
                                                       "🚨 ¡CITA DISPONIBLE PARA HUELLAS EN TORTOSA!"
                                                   )
                                  else:
                                                   print(
                                                       "⏳ No appointment available."
                                                   )
                 except Exception as e:
                                  print("❌ Error:", e)

                 time.sleep(5)  # Every 10 minutes
