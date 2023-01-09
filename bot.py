from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def random_joke():
    with open('anecdotes.txt', 'r', encoding='UTF-8') as jokes:
        lines = jokes.readlines()
        random_line = random.choice(lines).strip()
        return random_line



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЭто бот, который радует пользователей анекдотами. Напиши /help, чтобы получить "
                        "справку.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(
        "Наберите /start - для начала работы. Наберите /help для справки. Наберите /joke для получения анекдота! ")



@dp.message_handler(commands=['joke'])
async def process_help_command(message: types.Message):
    await message.reply(random_joke())


if __name__ == '__main__':
    executor.start_polling(dp)
