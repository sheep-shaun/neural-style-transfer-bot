from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/change_style")
        ]
    ],
    resize_keyboard=True,
)

selection_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Выбрать стиль из предложенных"),
            KeyboardButton(text="Отправить свой стиль")
        ]
    ],
    resize_keyboard=True,
)
