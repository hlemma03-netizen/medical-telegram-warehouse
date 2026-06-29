import asyncio
import json
import logging
import os
from datetime import datetime
from telethon import TelegramClient
from config import API_ID, API_HASH

CHANNELS = [
    "CheMed123",
    "lobelia4cosmetics",
    "tikvahpharma"
]

client = TelegramClient("telegram_session", API_ID, API_HASH)


async def scrape_channel(channel):
    messages = []

    os.makedirs(f"data/raw/images/{channel}", exist_ok=True)

    async for message in client.iter_messages(channel):

        msg = {
            "message_id": message.id,
            "date": str(message.date),
            "text": message.message,
            "views": message.views,
            "forwards": message.forwards,
            "has_media": message.photo is not None
        }

        messages.append(msg)

        # download image if exists
        if message.photo:
            await client.download_media(
                message,
                file=f"data/raw/images/{channel}/{message.id}.jpg"
            )

    # save JSON after finishing channel
    today = datetime.today().strftime("%Y-%m-%d")
    os.makedirs(f"data/raw/telegram_messages/{today}", exist_ok=True)

    with open(f"data/raw/telegram_messages/{today}/{channel}.json", "w") as f:
        json.dump(messages, f, indent=4)


async def main():
    await client.start()

    for channel in CHANNELS:
        try:
            print(f"Scraping {channel}...")
            logging.info(f"Started scraping {channel}")
            await scrape_channel(channel)
            logging.info(f"Finished scraping {channel}")
        except Exception as e:
            logging.error(f"Error scraping {channel}: {e}")

asyncio.run(main())
