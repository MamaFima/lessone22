from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio
from keyboards1 import reply_keyboard, inline_keyboard_links, inline_keyboard_more, inline_keyboard_options
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Добро пожаловать в чат!", reply_markup=reply_keyboard)

@dp.message(F.text == 'Привет')
async def greet_user(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == 'Пока')
async def say_goodbye(message: types.Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

@dp.message(Command('links'))
async def send_links(message: types.Message):
    await message.answer("Выберите ссылку:", reply_markup=inline_keyboard_links)

@dp.message(Command('dynamic'))
async def show_dynamic_buttons(message: types.Message):
    await message.answer("Хотите узнать больше?", reply_markup=inline_keyboard_more)

@dp.callback_query(F.data == 'show_more')
async def show_more_options(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text="Выберите опцию:", reply_markup=inline_keyboard_options)

@dp.callback_query(F.data.in_({'option_1', 'option_2'}))
async def option_selected(callback_query: types.CallbackQuery):
    option_text = "Опция 1" if callback_query.data == "option_1" else "Опция 2"
    await callback_query.message.answer(f"Вы выбрали: {option_text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
