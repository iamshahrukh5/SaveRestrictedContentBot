#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("17071170", default=None, cast=int)
API_HASH = config("b599a44ab247af88748ee04dc74756bd", default=None)
BOT_TOKEN = config("6059578267:AAHv5fADZU77RZx9otBtJApi8VA7mRjjIoY", default=None)
SESSION = config("BQADrPe2owmFJkl4sKXfgA8BmVquhRy4aphDi4cZ8rweiNDRsGeTkbaIU_50Si4t-ZYhsTEgF43pZLWNWo10Jv8_PQgTXeHnWQc897_51gtFrwsrVrzO0pQW_En2YysoQGf-ayTfW1c2gN0VH44xGyuXBgdFDuW4A369uGYp_gPq1R9UW5k1v6mZWAtxeYx0IFo05b0hItuVc_OOXzbouhstgnsaaGhFyLc8_AS_FT-IiYOJAzCbPHtph4KnI4fb6697Ef48HYApHhgdIu0fAeI57_1XcCkBEK1HihRsEa4cVferMAL3yRspmgYiL4Ezo4ei_bstbblYocPss3nb_mf3VgmZiwA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
