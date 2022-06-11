import requests
from pprint import pprint
import asyncio

updates = requests.get("https://api.telegram.org/bot5549698646:AAHNoGhONepTi4AI7CXT8JMgsyxcuPWcRTc/getUpdates").json()

len_sp = len(updates['result'])

async def answer():
    global len_sp
    while True:
        updates = requests.get(
            "https://api.telegram.org/bot5549698646:AAHNoGhONepTi4AI7CXT8JMgsyxcuPWcRTc/getUpdates").json()
        text_last_message = updates['result'][-1]['message']['text']
        chat_id = updates['result'][-1]['message']['chat']['id']
        if len_sp != len(updates['result']):
            requests.get(f'https://api.telegram.org/bot5549698646:AAHNoGhONepTi4AI7CXT8JMgsyxcuPWcRTc/sendMessage?chat_id={chat_id}&text={text_last_message}')
            len_sp = len(updates['result'])

loop = asyncio.get_event_loop()
asyncio.ensure_future(answer())
loop.run_forever()
# pprint(chat_id)
