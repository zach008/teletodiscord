import requests
from telethon import TelegramClient, events
import asyncio
import os

# Telegram credentials
api_id = '29333540'
api_hash = '5537b0d0ab4dff23413cf153a09df23d'
username = '+12066880957'

# Discord webhook URL
discord_webhook_url = 'https://discordapp.com/api/webhooks/1315041470423502919/D7kMcx6OIKCwH8pQMBN7K9sNTF6RFkWpdq9_ANSObScpygnSBRn7cX-WwmDT1Cb-DyZn'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    print("Telegram client created and started.")

    target = 'TEST0sa'

    @client.on(events.NewMessage(chats=target))
    async def handler(event):
        if event.photo:
            await handle_new_photo(event)

    print(f"Listening for new messages in {target}...")
    await client.run_until_disconnected()

async def handle_new_photo(event):
    # Download the photo
    photo_path = await event.download_media()
    print(f"Downloaded photo to {photo_path}")

    # Prepare payload for Discord
    payload = {
        "content": event.message.text or ""
    }

    # Read the image file
    with open(photo_path, 'rb') as f:
        files = {
            'file': (os.path.basename(photo_path), f)
        }
        # Send the POST request
        response = requests.post(discord_webhook_url, data=payload, files=files)

    if response.status_code == 204:
        print("Successfully sent to Discord.")
    else:
        print(f"Failed to send to Discord. Status code: {response.status_code}, Response: {response.text}")

    # Optionally, delete the photo after sending
    os.remove(photo_path)

client.loop.run_until_complete(main())