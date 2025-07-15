import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommandScopeAllPrivateChats
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from commands.commands import commands
from handlers.private_handler import router 
from handlers.exchanger_handler import ex_router

bot = Bot(os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_router(router)
dp.include_router(ex_router)

ALLOWED_UPDATES = [
    'message',
    'edited_message',
    'callback_query',
    'business_message',
    'business_connection',
    'edited_business_message'
]

async def main():
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('bot_logs.log', encoding='utf-8')
        ]
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

    
if __name__ == '__main__':
    asyncio.run(main())
