import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from info import START_IMG
from script import Script


# Telegram Bot API Request
async def api_request(client, method, data):
    url = f"https://api.telegram.org/bot{client.bot_token}/{method}"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            result = await response.json()

            if not result.get("ok"):
                raise Exception(result.get("description"))

            return result["result"]


# Styled Button Helper
def button(text, callback_data=None, url=None, style=None):
    data = {"text": text, "style": style}

    if callback_data:
        data["callback_data"] = callback_data

    if url:
        data["url"] = url

    return data


# Start Page Buttons
def start_buttons():
    return {
        "inline_keyboard": [
            [
                button("🏡", callback_data="home", style="primary"),
                button("🛡️", callback_data="shield", style="primary"),
                button("💳", callback_data="about", style="primary"),
            ],
            [
                button("💸", callback_data="premium", style="primary"),
                button("🖥️", callback_back="stats", style="danger"),
            ],
            [
                button(
                    "• MOVIE SEARCH GROUP •",
                    url="https://t.me/your_group_link",
                    style="primary"
                )
            ]
        ]
    }


# About Page Buttons
def about_buttons():
    return {
        "inline_keyboard": [
            [
                button("🔙 BACK", callback_data="home", style="danger")
            ]
        ]
    }


# Start Command
@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):

    msg = await message.reply_photo(
        photo=START_IMG,
        caption=Script.START_TXT.format(message.from_user.mention)
    )

    await api_request(client, "editMessageReplyMarkup", {
        "chat_id": msg.chat.id,
        "message_id": msg.id,
        "reply_markup": start_buttons()
    })


# Callback Handler
@Client.on_callback_query()
async def callback_handler(client: Client, query: CallbackQuery):

    if query.data == "about":

        await query.message.edit_caption(
            caption=Script.ABOUT_TXT
        )

        await api_request(client, "editMessageReplyMarkup", {
            "chat_id": query.message.chat.id,
            "message_id": query.message.id,
            "reply_markup": about_buttons()
        })

        await query.answer()

    elif query.data == "home":

        await query.message.edit_caption(
            caption=Script.START_TXT.format(query.from_user.mention)
        )

        await api_request(client, "editMessageReplyMarkup", {
            "chat_id": query.message.chat.id,
            "message_id": query.message.id,
            "reply_markup": start_buttons()
        })

        await query.answer()

    else:
        await query.answer(
            "Jald hi add hoga!",
            show_alert=False
        )
