from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.forMusic import menuKonsta, menuMassa, menuChiqish
from keyboards.default.menu import menu

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("menu dan bitasini talang", reply_markup=menu)


@dp.message_handler(text="Konsta musiqalari")
