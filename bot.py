import telethon
from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 12345
api_hash = 'your api id'
#!/usr/bin/env python3
# A simple script to print some messages.
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
proxy = None  # https://github.com/Anorov/PySocks

# Create and start the client so we can make requests (we don't here)
client = TelegramClient(session, api_id, api_hash, proxy=proxy).start()
groupentity = await client.get_entity(-123456)

# `pattern` is a regex, see https://docs.python.org/3/library/re.html
# Use https://regexone.com/ if you want a more interactive way of learning.
#
# "(?i)" makes it case-insensitive, and | separates "options".
@client.on(events.NewMessage(pattern=r'(?i).*\b(.*michael.*|.*john.*|.*frank.*)\b'))
async def handler(event):
        print ('someone mentioned')
        sender = await event.get_sender()
        name = utils.get_display_name(sender)
        user = client.get_entity
        mess_id = int(event.message.id)
        await client.forward_messages(groupentity, mess_id, sender, silent=None)
        notification_message = ('New mention\n\n\nText:\n\n' + event.message.message + '\n\n\nSent by: ' + name)
        await client.send_message(groupentity, notification_message)


@client.on(events.NewMessage(incoming=True))
async def replier(event):
        if event.message.mentioned:
            print ('someone replied')
            sender = await event.get_sender()
            name = utils.get_display_name(sender)
            user = client.get_entity

            mess_id = int(event.message.id)
            chat_name = 'chat name (i have to find the chat name)'
            await client.forward_messages(groupentity, mess_id, sender, silent=None)
            notification_message = ('New reply\n\n\nText:\n\n' + event.message.message + '\n\n\nSent by: ' + name + '\n\nChat name: \n\n' + chat_id)
            await client.send_message(groupentity, notification_message)
    
try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()

# Note: We used try/finally to show it can be done this way, but using:
#
#   with client:
#       client.run_until_disconnected()
#
# is almost always a better idea.
