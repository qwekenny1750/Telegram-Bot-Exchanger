from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Get the course 💶')],
        [
            KeyboardButton(text='Technosupport ⚙️'),
            KeyboardButton(text='All commands')
        ]
    ],
    resize_keyboard=True
)