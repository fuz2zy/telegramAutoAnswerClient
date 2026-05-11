import time
import os

from telethon.sessions import StringSession
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()


API_ID = int(os.getenv("API_ID"))
API_HASH = str(os.getenv("API_HASH"))
STRING_SESSION = str(os.getenv("STRING_SESSION"))

autoanswer_audio_path = "audio.ogg"

autoanswer_text = """
<blockquote>📞 Вы позвонили Царю Батюшке 🤴🏻. В начале разговора, приподите на колено и произнесите: Здравствуй, надеже государь, Свет наш и заступник, Солнышко красное, Отец родной. Беспокоящий тебя холоп, челом тебе бьет. Не вели казнить, а вели слово молвить</blockquote>
                      
<b>Царь Батюшка был оповещен о вашем обращении и вскоре ответит ✍🏻</b>
"""

last_active_time = time.time()
answers_info = {}

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)