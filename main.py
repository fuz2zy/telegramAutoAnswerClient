import asyncio
import config

from telethon import events

from handlers import update_autoanswer, autoanswer_handler, on_link_from_friend, on_video_from_bot


@config.client.on(events.NewMessage(outgoing=True))
async def on_new_message(event: events.NewMessage.Event):
    update_autoanswer()


@config.client.on(events.NewMessage(incoming=True))
async def on_private_message(event: events.NewMessage.Event):
    await autoanswer_handler(event)
    await on_link_from_friend(event)
    await on_video_from_bot(event)


async def main():
    print("автоответчик начал работу")
    await config.client.start()
    await config.client.run_until_disconnected()


asyncio.run(main())