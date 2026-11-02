from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from info import START_IMG
from script import Script

# Start Page ke buttons
def start_buttons():
    return InlineKeyboardMarkup([
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
    ])

# About Page ke buttons (Wapas aane ke liye Back button)
def about_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔙 BACK", callback_data="home")
        ]
    ])

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=Script.START_TXT.format(message.from_user.mention),
        reply_markup=start_buttons()
    )

@Client.on_callback_query()
async def callback_handler(client: Client, query: CallbackQuery):
    if query.data == "about":
        # 💳 dabane par caption badal kar ABOUT_TXT ho jayega
        await query.message.edit_caption(
            caption=Script.ABOUT_TXT,
            reply_markup=about_buttons()
        )
        await query.answer()

    elif query.data == "home":
        # 🔙 dabane par wapas original START_TXT aa jayega
        await query.message.edit_caption(
            caption=Script.START_TXT.format(query.from_user.mention),
            reply_markup=start_buttons()
        )
        await query.answer()

    else:
        await query.answer("Jald hi add hoga!", show_alert=False)
        
