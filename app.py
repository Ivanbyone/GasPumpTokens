""" """
import os
import logging
import asyncio
from pathlib import Path

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command

from src.gasPump.main import GPRequests

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

bot_logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    bot_logger.info('Bot has been started...')

    await dp.start_polling(bot)


@dp.message(Command("find"))
async def send_new_token(message: Message) -> None:
    if message.from_user.id == 606174532:
        while True:
            request = await GPRequests.make_regular_requests(interval=3)
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="on GasPump", url="https://t.me/gasPump_bot/app?startapp=eyJyZWZfdXNlcl9pZCI6NjA2MTc0NTMyfQ")]
            ])
            await bot.send_photo(-1002083243701,
                                 photo=f"{request['image_url']}",
                                 caption=f'New Token: {request["name"]}\nTicker: ${request["ticker"]}\nAddress: {request["token_address"]}',
                                 reply_markup=keyboard)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Unknown command")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Starting bot failed with {e}")
