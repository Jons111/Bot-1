from aiogram.dispatcher.filters.state import State,StatesGroup

class Forma(StatesGroup):
    Ism_qabul_qilish = State()
    Fam_qabul_qilish = State()
    Yosh_qabul_qilish = State()
    Kasb_qabul_qilish = State()
    Tel_qabul_qilish = State()

    tasdiqlash = State()