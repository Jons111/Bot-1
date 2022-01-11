from aiogram import types
from keyboards.default import matematik
from loader import dp


# Echo bot
@dp.message_handler(commands='amallar')
async def bot_echo(message: types.Message):
    await message.answer(text='matematik amallar botiga hush'
                              ' kelibsiz quyidagi'
                              ' amallardan birini tanlang',reply_markup=matematik.tugmalar)
