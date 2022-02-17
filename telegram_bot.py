# https://www.youtube.com/watch?v=I8K3iYcxPl0&list=RDCMUC7f5bVxWsm3jlZIPDzOMcAg&start_radio=1&rv=I8K3iYcxPl0&t=158

# https://www.youtube.com/watch?v=i5qHdtq4PSI&list=PLwVBSkoL97Q3phZRyInbM4lShvS1cBl-U&index=11&t=0s

# https://github.com/Latand/telegram-bot-lessons/blob/1d5cc91452e532d6d2a176759766b7226efa0532/lesson-7/keyboards/inline/menu_keyboards.py#L13


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from bot_requests import *
import logging
import filters
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random
from filters import IsAdminFilter




logging.basicConfig(level=logging.INFO)
if os.path.exists("env.py"):
    import env

# bot init

bot = Bot(token=env.TOKEN)

dp = Dispatcher(bot)

# activate filter_messages
dp.filters_factory.bind(IsAdminFilter)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Hi {0.first_name}'.format(message.from_user),
                           reply_markup=nav.mainMenu)


# remove new user joined messages
# @dp.message_handler(content_types=["new_chat_members"])
# async def on_user_joined(message: types.Message):
#     await message.delete()

#
# # ban command (admins only!)
# @dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
# async def cmd_ban(message: types.Message):
#     if not message.reply_to_message:
#         await message.reply("Эта команда должна быть ответом на сообщение!")
#         return
#     await message.bot.delete_message(config.GROUP_ID, message.message_id)
#     await message.bot.kick_chat_member(chat_id=config.GROUP_ID,
#                                        user_id=message.reply_to_message.from_user.id)
#     await message.reply_to_message.reply("Пользователь забанен!")


# echo
# @dp.message_handler()
# async def filter_messages(message: types.Message):
#     if "плохое слово" in message.text:
#         await message.delete()
#     elif "fetch" in message.text:
#         bot_requests.get_request()
# else:
#     await message.answer(message.text)


# fetch data from the server
@dp.message_handler(is_admin=True, commands=["fetch"], commands_prefix="!/")
async def cmd_fetch(message: types.Message):
    get_request()


# display menu
@dp.message_handler()
async def bot_menu(message: types.Message):
    if message.text == "Мои Заявки":
        user_orders = list(get_user_orders('1'))
        await bot.send_message(message.from_user.id,
                               "У вас сегодня" + str(
                                   len(user_orders)) + " заявок.",
                               reply_markup=nav.btnMain)
        await bot.send_message(message.from_user.id,
                               'ФИО: ' + str((user_orders[0]['name'])) + '\n' +
                               'Метро: ' + str(
                                   (user_orders[0]['tube'])) + '\n' +
                               'Адрес: ' + str(
                                   (user_orders[0]['address'])) + '\n' +
                               'Тел: ' + str(
                                   (user_orders[0]['phone_number'])) + '\n' +
                               'Время: ' + str(
                                   (user_orders[0]['time'])) + '\n' +
                               'Заявка: ' + str(
                                   (user_orders[0]['work_required'])) + '\n' +
                               'worker_id: ' + str(
                                   (user_orders[0]['worker_id'])) + '\n' +
                               'user_id: ' + str(message.from_user.id),
                               reply_markup=nav.btnMain)

    elif message.text == "Главное меню":
        await bot.send_message(message.from_user.id, "Главное меню",
                               reply_markup=nav.mainMenu)
    elif message.text == "Создать заявку":
        await bot.send_message(message.from_user.id, "Веедите текст в формате: " + '\n' +
                               "время(11-12), имя, телефон, адресс, заметки")
        await bot.send_message(message.from_user.id, "Меню клиентов",
                               reply_markup=nav.clientMenu)

    elif message.text == "Другое":
        await bot.send_message(message.from_user.id, "Другое",
                               reply_markup=nav.otherMenu)

    elif message.text == "Info":
        await bot.send_message(message.from_user.id, "Info")

    elif message.text == "Current Stock price":
        await bot.send_message(message.from_user.id, "Current Stock price"
                               )
    else:
        await message.reply("Uknown command")




# run long-polling

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
