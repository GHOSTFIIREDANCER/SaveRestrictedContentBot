#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = int(os.environ.get("API_ID", "22320226"))
API_HASH = os.environ.get("API_HASH", "8bfcf80120b231fc50863964059e5dab")
BOT_TOKEN = os.environ.get("BOT_TOKEN","6190235800:AAEC-tyRdT63uyd7O1olebNMLMpfddjBa4o")
SESSION = str(os.environ.get("SESSION","BQFUlGIAGiW-hLGRzE_J5KrWh9ziybCGxFMgNwjpSvFxAsKHiylVZFJnGaahkH4uL4IPO3DPw53uizKoUoWDFIqnPWfVWKb06J_djtlBGRChLVu33oaOMZeUtPALKRB0b4QisY1jvOnfMgvi9PxeM6_4y42Pt6PV18nNd96TCQa_j5v1aGfdMbMNUSgpE6fnDjlOt04ILKCDct6Rt6u8m9OsHx3d6t-_k_UsXcSuq5737xVxcxv9SE4QKb1s8x2vL0Teqvd56YAwDwWGlAgi31K3yHJa23X-9sLBCLwO539BqICLq-7fN06JBjaj8TLNJuK9nq5R8hpg0i2W95dFCSOLwWSq6gAAAAFa4LqeAA"))
AUTH = int(os.environ.get("BOT_OWNER", " 5819644574"))
FORCESUB = config("FORCESUB","zavia")

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
