#Импортируем нужные библиотеки и модули
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

#Пишем асинхронную функцию старта
async def on_startup(_):
    print('Бот вышел в онлайн')# Выводим сообщение в отдельный бат файл
    sqlite_db.sql_start() #Стартует БД (испоьзуйте sqlite)

#импортитуем хэндлеры
from handlers import client, admin, other
#регистрируем хэндлеры
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
