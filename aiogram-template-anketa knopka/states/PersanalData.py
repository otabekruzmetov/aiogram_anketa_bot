from aiogram.dispatcher.filters.state import StatesGroup, State

class PersanalData(StatesGroup):
    fullname = State()
    email = State()
    phoneNum = State()