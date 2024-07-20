import asyncio
import logging
import threading
from datetime import datetime
import pytz
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.messages import SendMessageRequest

# Configuration
API_ID = '25965226'
API_HASH = '7a1c735626be2bbb5b0898d66a47e15d'
STRING_SESSION = '1BJWap1sAULWi9iGmu16sNunlpMWoxxkrbHAEFo9aLt0C2dRVUe1Zsnk0Wj96sSv6kHBixqe_V5Dj8fdM9NQflXgRQTYKvSX90KdAlhpUsD6vO8kAo1VxlRyAXsSl39J88JjSlWZqwaXPYiO1Nw6fUD99ORSM14TNJUzKADLOfretST9t00tEtnOpKLkyi9FJTDqxF3fvMZwxRG0viqoLpPTU5s5IrwcS0Q-FmuqpgvX8rGXse8pwGEDz2hHC1olenumx-5-tnmzFYWgj_lslXtRr9HGI0Jm6xrcOHuCuP0l7ntAloN-h3CcW3teh6OyLSNmj9xJaySS2EOIHr2wH8qTKKr5faDQ='
UPDATE_INTERVAL = 20  # seconds
ERROR_RETRY_INTERVAL = 60  # seconds
LAST_NAME = '.'  # Replace with your last name

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_stockholm_time():
    """Get the current hour and minute in Stockholm."""
    tz = pytz.timezone('Europe/Stockholm')
    stockholm_time = datetime.now(tz)
    return stockholm_time.strftime('%H:%M')

async def keep_online():
    async with TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH) as client:
        logger.info("Client started.")
        
        # Get your own user ID
        me = await client.get_me()
        user_id = me.id  # or me.username if you prefer to use username
        
        while True:
            try:
                # Get current time in Stockholm and format the bio and message
                stockholm_time = get_stockholm_time()
                bio_message = f"{LAST_NAME} - {stockholm_time}"
                message_text = f"Current time in Stockholm: {stockholm_time}"
                
                # Update the profile bio with the formatted message
                await client(UpdateProfileRequest(
                    last_name=bio_message
                ))
                logger.info(f"Bio updated to: {bio_message}")
                
                # Send a message to yourself

                
                await asyncio.sleep(UPDATE_INTERVAL)  # Wait for the specified interval
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                await asyncio.sleep(ERROR_RETRY_INTERVAL)  # Wait longer if an error occurs

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # Run the Telegram client keep_online function
    asyncio.run(keep_online())
