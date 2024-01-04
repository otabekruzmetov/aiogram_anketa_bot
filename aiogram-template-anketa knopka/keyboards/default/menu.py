from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Konsta Musiqalari"),
            KeyboardButton(text="Massa musiqalari")
        ],
    ],

    resize_keyboard=True
)