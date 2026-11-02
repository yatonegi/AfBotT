from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from info import START_IMG
from script import Script

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    # Buttons layout jaisa screenshot me hai
    buttons = [
        [
            InlineKeyboardButton("🏡", callback_data="home"),
            InlineKeyboardButton("🛡️", callback_data="shield"),
            InlineKeyboardButton("💳", callback_data="about"),
            InlineKeyboardButton("💸", callback_data="premium"),
            InlineKeyboardButton("🖥️", callback_data="stats"),
        ],
        [
            InlineKeyboardButton("• MOVIE SEARCH GROUP •", url="https://t.me/your_group_link")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    # Photo ke saath caption bhejne ke liye
    await message.reply_photo(
        photo=START_IMG,
        caption=Script.START_TXT.format(message.from_user.mention),
        reply_markup=reply_markup
    )

# Callback queries handle karne ke liye (jaise card/about button click hone par)
@Client.on_callback_query()
async def callback_handler(client: Client, query):
    if query.data == "about":
        await query.answer("Bot maintained by YATO!", show_alert=True)
    else:
        await query.answer("Button Clicked!", show_alert=False)
      
