from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_hello = KeyboardButton(text='Привет')
button_bye = KeyboardButton(text='Пока')

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_hello, button_bye]],
    resize_keyboard=True
)

inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://lenta.ru/")],
    [InlineKeyboardButton(text="Музыка", url="https://music.youtube.com/")],
    [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
])

inline_keyboard_more = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
])

inline_keyboard_options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
    [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
])

