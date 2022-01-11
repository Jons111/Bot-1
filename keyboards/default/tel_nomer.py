from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

tel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kontakt",request_contact=True)
        ],

    ],
  resize_keyboard=True
)