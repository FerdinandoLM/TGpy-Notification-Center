from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 839749
api_hash = '00b6789108a2382989838012e2cid88e'
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


# `pattern` is a regex, see https://docs.python.org/3/library/re.html
# Use https://regexone.com/ if you want a more interactive way of learning.
#
# "(?i)" makes it case-insensitive, and | separates "options".
@client.on(events.NewMessage(pattern=r'(?i).*\b(yourname.*|yournickname.*|yourothername.*)\b'))
async def handler(event):
		
        print ('someone mentioned')
        groupentity = await client.get_entity(-12345)
        sender = await event.get_sender()
        name = utils.get_display_name(sender)
        user = client.get_entity
        mess_id = str(event.message.id)
        await event.forward_to(groupentity)
        chat_name = (await event.get_chat()).title
        chat_id = str((await event.get_chat()).id)
        messlink = str('https://t.me/c/' + str(chat_id) + '/' + str(mess_id))
        notification_message = ('#M' + '\n|\nChat: '+ str(chat_name) + ' | Chat ID: ' + str(chat_id) +' | Message ID: '+str(mess_id)+'\n|\nMessage Link: '+str(messlink) + '\n|\nSent by: ' + str(name) + '\n|\nText: \n' + str(event.message.message)+'\n|\nNew Mention')
        await client.send_message(groupentity, notification_message)


@client.on(events.NewMessage(incoming=True))
async def replier(event):
        if event.message.mentioned:
            print ('someone replied')
            groupentity = await client.get_entity(-12345)
            sender = await event.get_sender()
            name = utils.get_display_name(sender)
            user = client.get_entity
            mess_id = event.message.id
            await event.forward_to(groupentity)
            chat_name = (await event.get_chat()).title
            chat_id = str((await event.get_chat()).id)
            messlink = str('https://t.me/c/' + str(chat_id) + '/' + str(mess_id))
            notification_message = ('#R' + '\n|\nChat: '+ str(chat_name) + ' | Chat ID: ' + str(chat_id) +' | Message ID: '+str(mess_id)+'\n|\nMessage Link: '+str(messlink) + '\n|\nSent by : ' + str(name) + '\n|\nText :\n' + str(event.message.message)+'\n|\nNew Reply')
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
