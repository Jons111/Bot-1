from aiogram import types
from random import randint
from loader import dp



@dp.message_handler(text = "Qo'shish")
async def bot_echo(message: types.Message):
    son1 = randint(1,100)
    son2 = randint(1,100)
    natija = son2+son1
    await message.answer(text=f'{son1} + {son2} =',)
