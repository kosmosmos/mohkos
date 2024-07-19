import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateStatusRequest

# Provided settings
API_ID = '25965226'
API_HASH = '7a1c735626be2bbb5b0898d66a47e15d'
STRING_SESSION = '1BJWap1sAULWi9iGmu16sNunlpMWoxxkrbHAEFo9aLt0C2dRVUe1Zsnk0Wj96sSv6kHBixqe_V5Dj8fdM9NQflXgRQTYKvSX90KdAlhpUsD6vO8kAo1VxlRyAXsSl39J88JjSlWZqwaXPYiO1Nw6fUD99ORSM14TNJUzKADLOfretST9t00tEtnOpKLkyi9FJTDqxF3fvMZwxRG0viqoLpPTU5s5IrwcS0Q-FmuqpgvX8rGXse8pwGEDz2hHC1olenumx-5-tnmzFYWgj_lslXtRr9HGI0Jm6xrcOHuCuP0l7ntAloN-h3CcW3teh6OyLSNmj9xJaySS2EOIHr2wH8qTKKr5faDQ='

async def keep_online():
    # Use StringSession to initialize the TelegramClient
    async with TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH) as client:
        print("Client started.")
        
        while True:
            try:
                # Update the status to online
                await client(UpdateStatusRequest(offline=False))
                print("Keeping online...")
                await asyncio.sleep(20)  # Wait for 20 seconds
            except Exception as e:
                print(f"An error occurred: {e}")
                await asyncio.sleep(60)  # Wait longer if an error occurs to avoid rapid retries

if __name__ == "__main__":
    asyncio.run(keep_online())
