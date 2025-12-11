from pyrogram import Client, filters
from pyrogram.types import Message
import os, random, logging

ASSETS = os.path.join(os.path.dirname(__file__), "assets")

def pick(folder):
    path = os.path.join(ASSETS, folder)
    if not os.path.isdir(path):
        return None
    files = [os.path.join(path, x) for x in os.listdir(path)]
    return random.choice(files) if files else None

def register_handlers(app: Client):

    @app.on_message(filters.command("hug"))
    async def hug(_, m: Message):
        try:
            target = m.reply_to_message.from_user.mention if m.reply_to_message else "everyone"
            media = pick("hug")
            caption = f"{m.from_user.mention} hugged {target} 🤗"
            if media:
                await m.reply_photo(media, caption=caption)
            else:
                await m.reply_text(caption)
        except Exception:
            logging.exception("hug error")
            await m.reply_text("❌ Error in /hug")

    @app.on_message(filters.command("slap"))
    async def slap(_, m: Message):
        try:
            target = m.reply_to_message.from_user.mention if m.reply_to_message else "someone"
            media = pick("slap")
            caption = f"{m.from_user.mention} slapped {target} 👋"
            if media:
                await m.reply_animation(media, caption=caption)
            else:
                await m.reply_text(caption)
        except Exception:
            logging.exception("slap error")
            await m.reply_text("❌ Error in /slap")

    @app.on_message(filters.command("waifu"))
    async def waifu(_, m: Message):
        try:
            media = pick("waifu")
            if media:
                await m.reply_photo(media, caption=f"✨ Waifu for {m.from_user.mention}")
            else:
                await m.reply_text("No waifu images found.")
        except Exception:
            logging.exception("waifu error")
            await m.reply_text("❌ Error in /waifu")
