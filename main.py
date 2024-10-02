import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN
import random
from gtts import gTTS
import os
from deep_translator import GoogleTranslator

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('audio.mp3')
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('voice.ogg')
    await message.answer_voice(voice)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('TG02.pdf')
    await bot.send_document(message.chat.id, doc)



@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
        "Тренировка 1:\\n1. Скручивания: 3 подхода по 15 повторений\\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\\n1. Подъемы ног: 3 подхода по 15 повторений\\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_training = random.choice(training_list)
    await message.answer(f"Это ваша мини-тренировка на сегодня:\n{rand_training}")

    tts = gTTS(text=rand_training, lang='ru')
    tts.save('training.mp3') #формат ogg - файл в виде голосового сообщения
    audio = FSInputFile('training.mp3') #формат ogg - файл в виде голосового сообщения
    await bot.send_audio(message.chat.id, audio)
    os.remove('training.mp3') #удаление файла ogg


@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=600', 'https://images.pexels.com/photos/59523/pexels-photo-59523.jpeg?auto=compress&cs=tinysrgb&w=600', 'https://images.pexels.com/photos/1526410/pexels-photo-1526410.jpeg?auto=compress&cs=tinysrgb&w=600']
    rand_photo = random.choice(list)
    await message.answer_photo(rand_photo, caption='Это очень крутая фотография!') #await message.answer(random.choice(list))

@dp.message(F.photo)
async def aiphoto(message: Message):
    list = ['Ого, какая интересная фотография!', 'Не понимаю что это такое', 'Пожалуйста, не отправляй мне больше такое!']
    await message.answer(random.choice(list))
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')


@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer("ИИ стал универсальным термином для приложений, которые выполняют сложные задачи, которые когда-то требовали участия человека, например, общение с клиентами в Интернете или игра в шахматы. Этот термин часто используется взаимозаменяемо с его подобластями, которые включают машинное обучение (ML) и глубокое обучение.")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n/start \n/photo \n/video \n/training \n/audio \n/voice \/doc \n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я бот. Напиши мне что-нибудь и я постараюсь тебе ответить!")


#@dp.message() #зеркальные ответы на все сообщения
#async def start(message: Message):
    #await message.send_copy(chat_id=message.chat.id)

translator = GoogleTranslator(source='auto', target='en')


@dp.message()
async def translate_and_voice(message: Message):
    translated = translator.translate(message.text)
    await message.answer(translated)


    tts = gTTS(text=translated, lang='en')
    tts.save('response.ogg')
    audio = FSInputFile('response.ogg')
    await bot.send_audio(message.chat.id, audio)

    os.remove('response.ogg')



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
