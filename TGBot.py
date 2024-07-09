from telegram import Bot
from telegram.error import TelegramError

# Define your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN'

def post_to_telegram(message, image_url, TELEGRAM_CHAT_ID):
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        
        # Send the image with a caption
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=image_url, caption=message)
        
        print("Message with image posted to Telegram successfully.")
    except TelegramError as e:
        print(f"Failed to post to Telegram: {e}")
