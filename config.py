import time
import os

from telethon.sessions import StringSession
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

DOWNLOADER_BOT_USERNAME = "uasaverbot"
AIMS_USERNAME = "pipiduster666"
FRIEND_USERNAME = "agraman09"

API_ID = int(os.getenv("API_ID"))
API_HASH = str(os.getenv("API_HASH"))
STRING_SESSION = str(os.getenv("STRING_SESSION"))

autoanswer_text = """
<blockquote>📞 Вы позвонили Царю Батюшке 🤴🏻. В начале разговора, приподите на колено и произнесите: Здравствуй, надеже государь, Свет наш и заступник, Солнышко красное, Отец родной. Беспокоящий тебя холоп, челом тебе бьет. Не вели казнить, а вели слово молвить</blockquote>
                      
<b>Царь Батюшка был оповещен о вашем обращении и вскоре ответит ✍🏻</b>
"""

last_active = time.time()
last_answer = {}

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)