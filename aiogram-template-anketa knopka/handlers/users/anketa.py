from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.PersanalData import PersanalData


@dp.message_handler(Command("anketa"), state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kriting")
    await PersanalData.fullname.set()


@dp.message_handler(state=PersanalData.fullname)
async def answer_fullme(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )
    await message.answer("Emailgizni kiriting")
    await PersanalData.next()


@dp.message_handler(state=PersanalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )


    await message.answer("Telefon raqamingizni kiriting")
    await PersanalData.next()

@dp.message_handler(state=PersanalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.set()

    await state.update_data(
        {"phone": phone}
    )

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "Quydagi malumotlar qabul qilindi"
    msg += f"Ismingiz - {name} \n"
    msg += f"Emailingiz - {email}\n"
    msg += f"Telefon rqamimgiz - {phone}"

    await message.answer(msg)

    await state.finish()