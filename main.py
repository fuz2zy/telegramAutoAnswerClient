import asyncio
import time
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = str(os.getenv("API_HASH"))

last_active = time.time()
last_answer = {}

client = TelegramClient("name", API_ID, API_HASH)


@client.on(events.NewMessage(outgoing=True))
async def on_new_message(event: events.NewMessage.Event):
    global last_active, last_answer
    last_active = time.time()
    last_answer = {}


@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def on_private_message(event: events.NewMessage.Event):
    if not time.time() - last_active > 600:
        return
👑
    sender_id = event.sender_id

    last_answer_time = last_answer.get(sender_id, 0)

    if not time.time() - last_answer_time > 600:
        return
    
    last_answer[sender_id] = time.time()

    await client.send_message(sender_id, """
<blockquote>📞 Вы позвонили Царю Батюшке 🤴🏻. В начале разговора, приподите на колено и произнесите: Здравствуй, надеже государь, Свет наш и заступник, Солнышко красное, Отец родной. Беспокоящий тебя холоп, челом тебе бьет. Не вели казнить, а вели слово молвить</blockquote>
                      
<b>Царь Батюшка был оповещен о вашем обращении и вскоре ответит ✍🏻</b>
""", parse_mode="html")


async def main():
    print("автоответчик начал работу")
    await client.start()
    await client.run_until_disconnected()


asyncio.run(main())