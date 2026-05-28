import os

# Telegram API Credentials
API_ID = int(os.getenv("API_ID", "20593740"))
API_HASH = os.getenv("API_HASH", "8935cba4839cf186259d575604b3b24f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")  # Isko deploy karte time bharenge

# Bot Basic Information
BOT_NAME = "DW Music"
BOT_USERNAME = "DWMusic_Bot"
OWNER_USERNAME = "Atul_Tiwari"

# Support Group aur Channel ke Links
SUPPORT_CHAT = "https://t.me/Dream_World_Group"
SUPPORT_CHANNEL = "https://t.me/DW_Music_Official"

# Start Screen Image
START_IMG_URL = os.getenv("START_IMG_URL", "https://graph.org/file/default_start.jpg")

# MongoDB URI (Aapka apna personal secure database link)
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://bharatkumar672208_db_user:4OCbENejtHkhYgQD@cluster0.xdbqnjd.mongodb.net/?appName=Cluster0")
