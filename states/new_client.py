from aiogram.dispatcher.filters.state import StatesGroup, State


class NewCustomer(StatesGroup):
    customer = State()
