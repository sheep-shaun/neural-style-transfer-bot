from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


image_selection = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('1 - "Звездная ночь"'),
        ],
        [
            KeyboardButton('2 - "Сидящая обнаженная"'),
        ],
        [
            KeyboardButton('3 - "Осеннее одиночество"'),
        ],
    ],
    resize_keyboard=True,
)
