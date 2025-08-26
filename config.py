import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "21157281"))
API_HASH = getenv("API_HASH", "cd16b814151c1439adefb3c3a09b6096")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7865291325:AAG7XG7cqBzSziaVEyr4jW2K6sKEety7yKA")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Lakshay3434:Tony123@cluster0.s63lu.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002116643591))

OWNER_ID = int(getenv("OWNER_ID", 7821072467)) 

OWNER = int(getenv("OWNER", 7821072467))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-244ce902-f5e3-4c52-94d6-b5c4bb4ab7e5")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/paradox-zenu/Samxempire",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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"
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hxh_bot_support")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/zenitsu_bot_support")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
STRING1 = "BQGWmGwAsLP0Fjxm9yLGCQeGXKTaEIegt2AAT0-7TyFbG-me9f8q-LhuAsZBL21OgILY5325jZKyDP2YXzyucn6bNaVP-G3nb9xPzfXpmTbAOJwmLooRRlWWjMXcBDNbGjeeLBVwY8LYHRzeRFCfs1QM4c9NupnZmbKhPSluDcmYX_DiXcmykF5IQzYD0BnL1WzjJMGfDZqfCk4jXaE19wG7sdGWybjGTVgesUfq6hQ8emjMvY1-pyxfYFRM8nhe24wR38961UC8ffuAj2wAT2x3u9H-ISrCImt6FwQ69oyu9gE2Ta7stmD3HtwSdf813vxB5RhO7ekU6z2j0aiW4JcbhYZCrAAAAAHgogBgAA" 
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/xl0xwt.jpg")
PING_IMG_URL = "https://files.catbox.moe/ae6lff.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://i.ibb.co/26BhmZS/photo-2025-01-05-21-59-21-7456554424085774344.jpg")
TELEGRAM_AUDIO_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
STREAM_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
