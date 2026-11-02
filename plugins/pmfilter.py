from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.text & filters.group)
async def auto_filter(client: Client, message: Message):
    # Filhaal basic test message check
    if message.text.lower() == "hi":
        await message.reply_text(f"Hello {message.from_user.first_name}!")
      
