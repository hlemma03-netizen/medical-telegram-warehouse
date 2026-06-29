from telethon import TelegramClient

async def scrape_channel(client, channel):
    async for message in client.iter_messages(channel):
        print({
            "message_id": message.id,
            "date": message.date,
            "text": message.message,
            "views": message.views,
            "forwards": message.forwards,
            "has_media": message.media is not None
        })
