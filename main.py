import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient

# config.py से डेटा इम्पोर्ट करना
try:
    from config import API_ID, API_HASH, MONGO_DB_URI, BOT_NAME, SUPPORT_CHAT, SUPPORT_CHANNEL
except ImportError:
    API_ID = int(os.getenv("API_ID", "20593740"))
    API_HASH = os.getenv("API_HASH", "8935cba4839cf186259d575604b3b24f")
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
    BOT_NAME = "DW Music"
    SUPPORT_CHAT = "https://t.me/atulsupport"
    SUPPORT_CHANNEL = "https://t.me/atulsupport12"

# आपका बॉट टोकन
BOT_TOKEN = "8917504249:AAGJs59WQDajnALwtXuUXBFQOurU5trJ3Lg"

# LOGGER ID
LOGGER_ID = -1003995231588

# बॉट क्लाइंट सेटअप
bot = Client(
    "dw_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# MongoDB कनेक्शन सेटअप
try:
    mongo = AsyncIOMotorClient(MONGO_DB_URI)
    db = mongo.DWMusicBot
    users_db = db.users
    print("Database connected successfully!")
except Exception as e:
    print(f"Database Connection Error: {e}")

# /start कमांड का हैंडलर
@bot.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    # यूजर को डेटाबेस में सेव करना
    try:
        await users_db.update_one(
            {"_id": user_id},
            {"$set": {"name": first_name}},
            upsert=True
        )
        # लॉग ग्रुप में मैसेज भेजना
        await client.send_message(LOGGER_ID, f"New User Started Bot: {first_name} (ID: {user_id})")
    except Exception as e:
        print(f"User save error: {e}")

    # वेलकम मैसेज
    welcome_text = (
        f"👋 **नमस्ते {first_name}!**\n\n"
        f"🎵 स्वागत है आपका **{BOT_NAME}** में।\n"
        f"यहाँ आप अपने पसंदीदा गानों को हाई क्वालिटी में डाउनलोड और स्ट्रीम कर सकते हैं।"
    )
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✨ ग्रुप सपोर्ट", url=SUPPORT_CHAT),
            InlineKeyboardButton("📢 ऑफिशियल चैनल", url=SUPPORT_CHANNEL)
        ]
    ])
    
    await message.reply_text(text=welcome_text, reply_markup=buttons)

# बॉट को चालू करना
if __name__ == "__main__":
    print("Bot is starting...")
    bot.run()
