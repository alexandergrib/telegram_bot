from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

# main menu
btnRandom = KeyboardButton('Мои Заявки')
btnCreateNew = KeyboardButton('Создать заявку')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnCreateNew, btnOther)

# other menu
btnInfo = KeyboardButton('Info')
btnMoney = KeyboardButton('Current Stock price')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)
