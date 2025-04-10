from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
import time

# Set up the bot with your API token
TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'  # Replace with your actual Telegram Bot API token
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
def greeting(update: Update, context):
    """Handle the /greeting command."""
    update.message.reply_text("Greetings! I hope you're having a great day!")

# Function for /status command
def status(update: Update, context):
    """Handle the /status command."""
    # You can add any status information here, like checking if the bot is active
    update.message.reply_text("Bot is active and working! All systems are good.")

# Main function to set up the bot and handle commands
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('time', time_command))
    dispatcher.add_handler(CommandHandler('delete', delete_previous))
    dispatcher.add_handler(CommandHandler('greeting', greeting))
    dispatcher.add_handler(CommandHandler('status', status))

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
