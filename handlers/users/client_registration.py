from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.new_client import NewCustomer


@dp.message_handler(Command("new_client"), state=None)
async def add_new_client(message: types.Message):
    await message.answer("Введите телефон клиента, \n"
                         "ФИО клиента, \n"
                         "Адресс клиента"
                         )

    # Вариант 1 - с помощью функции сет
    await NewCustomer.customer.set()


@dp.message_handler(state=NewCustomer.customer)
async def save_new_client(message: types.Message, state: FSMContext):
    answer = message.text
    new_client = answer.split(',')
    await state.update_data(
        {
           'new_client': answer
        }
    )
    await message.answer(f"Вы ввели: \n"
                         f"<b>Телефон:</b> {new_client[0]} \n"
                         f"<b>ФИО:</b> {new_client[1]} \n"
                         f"<b>Адрес:</b> {new_client[-1]} \n"
                         "Если данные неверны вы можете исправить их на сайте https://google.ru")
    await state.finish()
