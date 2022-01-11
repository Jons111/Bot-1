from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

inline_tugmalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Qo'shish" ,callback_data='1-amal'),
            InlineKeyboardButton(text="forma to'ldirish" ,callback_data='2-amal'),
        ],
        [
            InlineKeyboardButton(text='Ulashish',switch_inline_query="Zo'r bot ekan"),
            InlineKeyboardButton(text='Kanal',url='https://t.me/UstozShogird'),
        ]
    ]
)