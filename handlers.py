import time
import asyncio
import config

from telethon import events


async def update_autoanswer(event: events.NewMessage.Event):
    config.last_active_time = time.time()

    if event.is_private:
        chat = await event.get_chat()
        config.answers_info[chat.id] = 0


async def autoanswer_handler(event: events.NewMessage.Event):
    if event.is_private:
        if not time.time() - config.last_active_time > 600:
            return
        
        sender_id = event.sender_id
        user_answer_info = config.answers_info.get(sender_id, 0)
        
        if user_answer_info == 1:
            return
        
        
        config.answers_info[sender_id] = 1
        await asyncio.sleep(60)
        await config.client.send_message(sender_id, config.autoanswer_text, parse_mode="html")
