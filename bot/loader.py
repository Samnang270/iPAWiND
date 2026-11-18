import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.config import bot_token, accounts, reseller_accounts, api_id, api_hash
from bot.utils.r2 import R2Storage
from pyrogram import Client

# Initialize bot directly with Telegram's official cloud servers
bot = Bot(bot_token)

pyrogram_bot = Client(
    name="pyrobot", 
    api_id=api_id, 
    api_hash=api_hash, 
    bot_token=bot_token, 
    no_updates=True
)

dp = Dispatcher(bot, storage=MemoryStorage())

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

r2 = R2Storage(
    'https://7559de3627702042016e5211631ad5c3.r2.cloudflarestorage.com',
    '2f11df7945d6f9cd72ef3730316c0479',
    'c2e486e9e5c0489d53a6f61414cf182257836406e145c3478cf21c94dc3cabc0',
    'ipawind-apps', 
    'https://pub-5551ce10937a4badbfbd5aa34988fbf7.r2.dev'
)
