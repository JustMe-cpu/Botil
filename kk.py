import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start"), KeyboardButton(text="/help")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет!", reply_markup=keyboard)

@router.message(Command("help"))
async def help_handler(message: Message):
    commands = "/start - начать общение\n/help - список команд\n(Напишите что угодно, и бот повторит ваш текст)"
    await message.answer(commands)

@router.message()
async def echo_handler(message: Message):
    await message.answer(f"Ты написао: {message.text})

async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

