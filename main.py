from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
import time

# Set up the bot with your API token
TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'  # Replace with your actual Telegram Bot API token
bot = Bot(token=TOKEN)

# List to store the sent messages' IDs (you can extend this for more control)
sent_messages = []

# Function for /start command
def start(update: Update, context):
    """Handle the /start command."""
    user = update.message.from_user
    msg = update.message.reply_text(f"Hello {user.first_name}! I am your appointment checker bot. Use /help to see available commands.")
    sent_messages.append(msg.message_id)  # Store the message ID
    return

# Function for /time command
def time_command(update: Update, context):
    """Handle the /time command."""
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    msg = update.message.reply_text(f"Current server time is: {current_time}")
    sent_messages.append(msg.message_id)  # Store the message ID
    return

# Function for /delete command (Deletes all bot's messages in the chat)
def delete_all(update: Update, context):
    """Handle the /delete command."""
    user = update.message.from_user
    chat_id = update.message.chat_id
    
    # Delete all messages sent by the bot
    for message_id in sent_messages:
        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
            print(f"Deleted message {message_id}")
        except Exception as e:
            print(f"Failed to delete message {message_id}: {e}")
    
    sent_messages.clear()  # Clear the list after deleting all messages
    update.message.reply_text(f"Deleted all bot messages for {user.first_name}.")
    return

# Function for /greeting command
def greeting(update: Update, context):
    """Handle the /greeting command."""
    msg = update.message.reply_text("Greetings! I hope you're having a great day!")
    sent_messages.append(msg.message_id)  # Store the message ID
    return

# Function for /status command
def status(update: Update, context):
    """Handle the /status command."""
    # You can add any status information here, like checking if the bot is active
    msg = update.message.reply_text("Bot is active and working! All systems are good.")
    sent_messages.append(msg.message_id)  # Store the message ID
    return

# Function for /help command (Displays all available commands)
def help_command(update: Update, context):
    """Handle the /help command."""
    help_text = (
        "Here are the available commands:\n\n"
        "/start - Start the bot and get a welcome message.\n"
        "/time - Get the current server time.\n"
        "/delete - Delete all the bot's messages in the chat.\n"
        "/greeting - Send a greeting message from the bot.\n"
        "/status - Check the status of the bot.\n"
        "/help - Display this help message."
    )
    update.message.reply_text(help_text)
    return

# Main function to set up the bot and handle commands
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('time', time_command))
    dispatcher.add_handler(CommandHandler('delete', delete_all))  # Changed to delete all messages
    dispatcher.add_handler(CommandHandler('greeting', greeting))
    dispatcher.add_handler(CommandHandler('status', status))
    dispatcher.add_handler(CommandHandler('help', help_command))  # Add /help command handler

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
