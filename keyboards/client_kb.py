from aiogram.types import ReplyKeyboardMarkup, KeyboardButton# ReplyKeyboardRemove
#Кнопки
b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

#Расположение кнопок
kb_client.add(b3).row(b4, b5). add(b1, b2)

