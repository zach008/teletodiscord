from telethon import TelegramClient
import asyncio

# Replace these with your actual credentials
api_id = '29333540'
api_hash = '5537b0d0ab4dff23413cf153a09df23d'

client = TelegramClient('session_name', api_id, api_hash)

async def list_channels():
    await client.start()
    print("Listing all channels and groups:")
    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            username = dialog.entity.username if hasattr(dialog.entity, 'username') else 'No username'
            print(f"Name: {dialog.name}, ID: {dialog.id}, Username: {username}")

if __name__ == '__main__':
    asyncio.run(list_channels())