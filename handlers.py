import time
import config

from telethon import events


def update_autoanswer():
    config.last_active = time.time()
    config.last_answer = {}


async def autoanswer_handler(event: events.NewMessage.Event):
    if event.is_private:
        if not time.time() - config.last_active > 600:
            return
        
        sender_id = event.sender_id
        last_answer_time = config.last_answer.get(sender_id, 0)

        if not time.time() - last_answer_time > 600:
            return
        
        config.last_answer[sender_id] = time.time()
        await config.client.send_message(sender_id, config.autoanswer_text, parse_mode="html")


async def on_video_from_bot(event: events.NewMessage.Event):
    sender = await event.get_sender()
    if sender.username == config.DOWNLOADER_BOT_USERNAME and event.video:
        await event.forward_to(config.AIMS_USERNAME)


async def on_link_from_friend(event: events.NewMessage.Event):
    sender = await event.get_sender()
    if sender.username == config.FRIEND_USERNAME and event.message.text and event.message.text[21] == "https://vt.tiktok.com":
        await event.forward_to(config.DOWNLOADER_BOT_USERNAME)
