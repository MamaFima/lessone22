import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.token import TokenValidationError
import requests
from deep_translator import GoogleTranslator
import asyncio
from config import OPENWEATHER_API_KEY, TOKEN_POGODA

API_TOKEN = TOKEN_POGODA
OPENWEATHER_API_KEY = OPENWEATHER_API_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я бот 'Предсказатель погоды'. Выбери город, и я расскажу тебе прогноз погоды.")


@dp.message(Command(commands=['city']))
async def get_city(message: types.Message):
    await message.answer("Введите город, для которого хотите узнать погоду:")


@dp.message(lambda message: 'спасибо' in message.text.lower())
async def thanks_reply(message: types.Message):
    await message.answer("Пожалуйста! Рад помочь 😊")

@dp.message(lambda message: not message.text.startswith('/') and 'спасибо' not in message.text.lower())
async def fetch_weather(message: types.Message):
    city = message.text
    weather_data = get_weather(city)

    if weather_data:
      
        translated_weather = GoogleTranslator(source='en', target='ru').translate(weather_data['description'])

        response = (
            f"Погода в городе {city}:\n"
            f"Температура: {weather_data['temp']}°C\n"
            f"Ощущается как: {weather_data['feels_like']}°C\n"
            f"Описание: {translated_weather.capitalize()}"
        )
    else:
        response = "Извините, я не могу найти погоду для этого города."

    await message.answer(response)


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        return None

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except TokenValidationError as e:
        logging.error(f"Token error: {e}")
