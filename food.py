import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from deep_translator import GoogleTranslator
import requests
from config import TOKEN


# Используем тестовый API ключ "1" для TheMealDB
API_URL = "https://www.themealdb.com/api/json/v1/1"
bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = GoogleTranslator(source='ru', target='en')

def get_meal_by_name(meal_name):
    response = requests.get(f'{API_URL}/search.php?s={meal_name}')
    return response.json()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Напиши мне название блюда, и я пришлю его рецепт и фотографию.")

@dp.message()
async def send_meal_info(message: Message):
    # Переводим название блюда на английский
    meal_name_russian = message.text
    meal_name_english = translator.translate(meal_name_russian)
  
    meal_data = get_meal_by_name(meal_name_english)

    if meal_data['meals']:
        meal = meal_data['meals'][0]  # Берем первое блюдо из результата
       
        meal_image = meal['strMealThumb'] + '/preview'
     
        translator_en_ru = GoogleTranslator(source='en', target='ru')
        translated_instructions = translator_en_ru.translate(meal['strInstructions'])
        
        info = (f"Блюдо: {meal['strMeal']}\n"
                f"Категория: {meal['strCategory']}\n"
                f"Кухня: {meal['strArea']}\n")

        instructions_part = f"Инструкции: {translated_instructions}"

        await message.answer_photo(meal_image, caption=info)
     
        if len(instructions_part) > 1024:
            for chunk in [instructions_part[i:i+1024] for i in range(0, len(instructions_part), 1024)]:
                await message.answer(chunk)
        else:
            await message.answer(instructions_part)
    else:
        await message.answer("Блюдо не найдено. Проверьте правильность написания и попробуйте еще раз.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
