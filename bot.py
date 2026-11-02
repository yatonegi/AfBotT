import os
from pyrogram import Client
from aiohttp import web
from info import API_ID, API_HASH, BOT_TOKEN
from web_server import web_server

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="LucyBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        print("Bot Started Successfully!")

        # Start dummy web server for Render port check
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        PORT = int(os.environ.get("PORT", 8080))
        await web.TCPSite(app, bind_address, PORT).start()
        print(f"Web service running on port {PORT}")

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped!")

if __name__ == "__main__":
    Bot().run()
    
