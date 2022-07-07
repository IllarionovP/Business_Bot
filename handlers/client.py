from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


answ = dict()

# Кнопка ссылка(люой адрес ссылки который вам надо)
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtu.be/72hKbPf0SzU')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://www.marieclaire.ru/food/znayut-vse-italyancy-sekrety-idealnoi-piccy-kotorye-prevratyat-ee-v-shedevr/')

urlkb.add(urlButton, urlButton2)


# @dp.message_handler(commands=['ссылки'])
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

#пост голосование
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='Не Like', callback_data='like_-1'))

# @dp.message_handler(commands='test')
async def test_commands(message : types.Message):
    await message.answer('Вы любите пиццу?'
                         ' /start', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)






#Команды
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_Sheef_MasterBot')

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Звездная 7')  # , reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=["Меню"])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

#Регистрируем хэндлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
    dp.register_message_handler(url_command, commands=['ссылки'])
    dp.register_message_handler(test_commands, commands=['test'])

