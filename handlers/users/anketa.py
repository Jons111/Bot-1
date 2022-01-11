from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ContentTypes
from states.holatlar import Forma
from loader import dp
from keyboards.default.tel_nomer import tel

# Echo bot

@dp.callback_query_handler(text = '2-amal')
async def xabar(malumot:CallbackQuery):
    await malumot.message.answer(text='Anketa to\'ldirish uchun ma\'lumotlaringizni kiriting')
    await  malumot.message.answer(text='Ismni kiriting')
    await Forma.Ism_qabul_qilish.set()
lugat = {}
@dp.message_handler(state=Forma.Ism_qabul_qilish )
async def ism_uchun(malumot:Message):
    name = malumot.text
    lugat['Ism']=name
    await  malumot.answer(text='Famni kiriting')
    await Forma.Fam_qabul_qilish.set()

@dp.message_handler(state=Forma.Fam_qabul_qilish)
async def ism_uchun(malumot:Message):
    fam = malumot.text
    lugat['Familya']=fam
    await  malumot.answer(text='Yoshni kiriting')
    await Forma.Yosh_qabul_qilish.set()

@dp.message_handler(state=Forma.Yosh_qabul_qilish )
async def ism_uchun(malumot:Message):
    yosh = malumot.text
    if not  yosh.isdigit():
        await  malumot.answer(text='Yoshni faqat raqam bilan  kiriting')
        await Forma.Yosh_qabul_qilish.set()
    else:
        lugat['Yosh']=yosh
        await  malumot.answer(text='Kasbni kiriting')
        await Forma.Kasb_qabul_qilish.set()


@dp.message_handler(state=Forma.Kasb_qabul_qilish )
async def ism_uchun(malumot:Message):
    kasb = malumot.text
    lugat['Kasb']=kasb
    await  malumot.answer(text='Telni kiriting')
    await Forma.Tel_qabul_qilish.set()

@dp.message_handler(state=Forma.Tel_qabul_qilish,content_types=ContentTypes.CONTACT )
async def ism_uchun(malumot:Message,state:FSMContext):
    tel = malumot.contact.phone_number
    print(tel)
    lugat['Tel']=tel
    user = malumot.from_user.username
    lugat['username']=user
    matn = ''
    for i in lugat:
        matn+=i +':'+lugat[i]+'\n'

    await state.finish()
    await malumot.answer(text=matn)
