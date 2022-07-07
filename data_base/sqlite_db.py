#импортитуем sqlite, бота из модуля
import sqlite3 as sq
from create_bot import bot


# функция запуска БД
def sql_start():
    global conect, cursor
    conect = sq.connect('pizza_cool.db')
    cursor = conect.cursor()
    if conect:
        print('Data base connected OK')
    conect.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    conect.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        conect.commit()


async def sql_read(message):
    for ret in cursor.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена - {ret[-1]} руб')


async def sql_read2():
    return cursor.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cursor.execute('DELETE FROM menu WHERE name == ?', (data,))
    conect.commit()
