import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=600', 'https://images.pexels.com/photos/59523/pexels-photo-59523.jpeg?auto=compress&cs=tinysrgb&w=600', 'https://images.pexels.com/photos/1526410/pexels-photo-1526410.jpeg?auto=compress&cs=tinysrgb&w=600']
    rand_photo = random.choice(list)
    await message.answer_photo(rand_photo, caption='Это очень крутая фотография!') #await message.answer(random.choice(list))

@dp.message(F.photo)
async def aiphoto(message: Message):
    list = ['Ого, какая интересная фотография!', 'Не понимаю что это такое', 'Пожалуйста, не отправляй мне больше такое!']
    await message.answer(random.choice(list))

@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer("ИИ стал универсальным термином для приложений, которые выполняют сложные задачи, которые когда-то требовали участия человека, например, общение с клиентами в Интернете или игра в шахматы. Этот термин часто используется взаимозаменяемо с его подобластями, которые включают машинное обучение (ML) и глубокое обучение.")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n/start \n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я бот. Напиши мне что-нибудь и я постараюсь тебе ответить!")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())