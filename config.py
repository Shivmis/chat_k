from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24280518"
# -------------------------------------------------------------
API_HASH = "ec5793b4bef624381b19ad2b6fd082f8"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "1808943146"))
SUPPORT_GRP = "Meetupzone_Chatting"
UPDATE_CHNL = "Ur_karma_baby"
OWNER_USERNAME = "introvertt_i"
