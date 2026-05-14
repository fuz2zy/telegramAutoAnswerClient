import time
import os

from telethon.sessions import StringSession
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()


API_ID = int(os.getenv("API_ID"))
API_HASH = str(os.getenv("API_HASH"))
STRING_SESSION = str(os.getenv("STRING_SESSION"))
AUTOANSWER_TEXT=str(os.getenv("AUTOANSWER_TEXT"))

last_active_time = time.time()
answers_info = {}

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)