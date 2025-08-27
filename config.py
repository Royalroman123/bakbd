import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28976608"))
API_HASH = getenv("API_HASH", "1e200bdfdcc3cc816f9f6a62e6e6f4a0")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "8389239648:AAHqaQJxJE3y7fzm3cyA8t2_p8c1PAmCBho")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1003063952141))

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
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Silent_world_chatting")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Silent_world_chatting")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = '7f92897a59464ddbbf00f06cd6bda7fc'
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
STRING1 = "BQG6JeAAmFhUUCSQ5IAfQ0yCdT6cs1l-2cyUdQ4rAKocQa2nYljlhwgQli10omZfaJ87VGUMJNv9_olSRw9qGEUjCHw1Ros33ESSKrE1-j1uEms8S3ygptVRH9NoTLRD1Yojbgtu1yj8oYoIhZu-Uog4i7d2EMTiGrTx1RZ8OrRlXGRrKXIhtqLqeqpb43qBoD3orzwRilVbHQ9beOYxhJx61LlPS-z9DcoUb9E7T4xFAS3bb9Q6oKNUCHlUM6goetnLp2tEk1WywCwF6j76urk34wr2x9GcWu6Mp6hSNcJyzDO3i834qWUzWCD3DrCHG_I4J-Ib8jz7_BMgu3zDnvdt-vJs6AAAAAHSdUy9AA" 
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


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/iyr906.jpg")
PING_IMG_URL = "https://files.catbox.moe/iyr906.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://files.catbox.moe/iyr906.jpg")
TELEGRAM_AUDIO_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
STREAM_IMG_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/bRDZXVJ4/photo-2025-08-27-06-03-03-7543141926845808648.jpg"

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














