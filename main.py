from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
import time

# Set up the bot with your API token
TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = Bot(token=TOKEN)

# Function for /start command
def start(update: Update, context):
    """Handle the /start command."""
    user = update.message.from_user
    update.message.reply_text(f"Hello {user.first_name}! I am your appointment checker bot. Use /help to see available commands.")

# Function for /time command
def time_command(update: Update, context):
    """Handle the /time command."""
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    update.message.reply_text(f"Current server time is: {current_time}")

# Function for /delete command
def delete_previous(update: Update, context):
    """Handle the /delete command."""
    user = update.message.from_user
    update.message.reply_text(f"Deleted previous messages for {user.first_name}.")

    # To actually delete the message, you can use the `delete_message` method
    # For example, if you want to delete the last message:
    bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id - 1)

# Function for /greeting command
def greeting
