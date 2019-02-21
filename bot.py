from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345
api_hash = '00fgc3dt53234f9f6f5b52e2714ab0e'
#!/usr/bin/env python3
# A simple script to get notified on telegram.
import os
import sys
import time

from telethon import TelegramClient, events, utils

import logging
logging.basicConfig(level=logging.WARNING)

def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)


session = os.environ.get('TG_SESSION', 'printer')
proxy = None

# Create and start the client so we can make requests (we don't here)
client = TelegramClient(session, api_id, api_hash, proxy=proxy).start()

# Insert your private chat ID where you want to receive the notifications
groupentity = await client.get_entity(-13456) 

# `pattern` is a regex, see https://docs.python.org/3/library/re.html
# Use https://regexone.com/ if you want a more interactive way of learning.
#
# "(?i)" makes it case-insensitive, and | separates "options".
@client.on(events.NewMessage(pattern=r'(?i).*\b(.*yourname.*|.*yournickname.*|.*somethingelse.*)\b'))
async def handler(event):
        print ('someone mentioned')

        sender = await event.get_sender()
        name = utils.get_display_name(sender)
        user = client.get_entity
        mess_id = event.message.id
        await event.forward_to(groupentity)
        chat_name = (await event.get_chat()).title
        chat_id = str((await event.get_chat()).id)
        notification_message = ('#NewReply' + '\n ---- \nChat Name: '+ chat_name + '\nChat ID: ' + chat_id + '\n ---- \n Sent by: ' + name + '\nText:\n' + event.message.message)
        await client.send_message(groupentity, notification_message)


@client.on(events.NewMessage(incoming=True))
async def replier(event):
        if event.message.mentioned:
            print ('someone replied')
            sender = await event.get_sender()
            name = utils.get_display_name(sender)
            user = client.get_entity
            mess_id = event.message.id
            await event.forward_to(groupentity)
            chat_name = (await event.get_chat()).title
            chat_id = str((await event.get_chat()).id)
            notification_message = ('#NewMention' + '\n ---- \nChat Name: '+ chat_name + '\nChat ID: ' + chat_id + '\n ---- \n Sent by: ' + name + '\nText:\n' + event.message.message)
            await client.send_message(groupentity, notification_message)
            
    
try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()