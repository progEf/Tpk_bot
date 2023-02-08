import asyncio
import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, callback_query
from aiogram.dispatcher.filters import Text
import schedule
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboard import kb_client, kb_client_1
from sokrashcheniya_url import shorten_url
from parsing_tpk import parsing_even_1, parsing_even_2, parsing_odd_1, parsing_odd_2, parsing, parsing_even_3, \
    parsing_odd_3, qwerasfzv,parsing_odd_12, parsing_odd_1221

from datetime import datetime, timedelta, timezone

from TR_y import dialog_2, dialog_3, dialog_4, dialog_5

storage = MemoryStorage()
TOKEN = '5981376324:AAGOzZ9770BSaeZXM4RLYhPVeCS-khGGg_E'
bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot, storage=storage)
from db_1 import Database
from baseUs import BASE_UESR_ID, BSD, con12, CON

db = Database('Tpk.db')


class dialog(StatesGroup):
    spam = State()
    blacklist = State()
    whitelist = State()


class dialog1(StatesGroup):
    spam = State()
    blacklist = State()
    whitelist = State()

class dialog8(StatesGroup):
    spam = State()
    blacklist = State()
    whitelist = State()

async def on_startup(_):
    print('Бот вышел онлайн')




@dp.message_handler(commands=['start', 'help'])
async def comand_start(message: types.message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    await  bot.send_message(message.from_user.id, 'Привет', reply_markup=kb_client)


def ce():
    c = []
    for i in parsing_even_2()[0], parsing_even_1()[0], parsing_odd_1()[0], parsing_odd_2()[0], parsing_odd_3()[0], \
             parsing_even_3()[0], parsing_odd_12()[0]:
        c.append(i)
    return c


@dp.message_handler(Text(equals='Расписание для студентов🧑‍🎓'))
async def cor12t(message: types.message, state: FSMContext):
    x = f'({str(message.chat.id)},)'

    x1 = x[1:-2]

    db.stude(1, x1)
    vis = db.see_stude()
    masivich_1 = []
    for ib in vis:
        c = str(ib)
        c1 = c[1:-2]
        c2 = int(c1)
        masivich_1.append(c2)

    db.add_mas_stud(sum(masivich_1))

    dec123 = CON(x1)
    for dec12 in dec123:
        dec_as = dec12[1:-2]

    if message.from_user.id == int(dec_as):
        for ITEG in con12(dec_as):
            global fr6
            fr6 = ITEG[1:-2]


        if len(fr6) >= 2:
            await bot.send_message(message.from_user.id, 'Слишком много попыток')
            await bot.send_message(message.from_user.id, f'Вы будете заблокированы на {30} секунд')
            prob = con12(x1)
            for dec in prob:
                dec1 = dec[1:-2]
                if int(dec1) >= 10:
                    await asyncio.sleep(20)
                    await dialog_5.whitelist.set()
                    db.cou_user_del(x1)
                    await state.finish()
                    await bot.send_message(message.from_user.id, f'Вы разблокированы')
                    db.cou_user_32(1, x1)

        else:
            for userog in BSD():
                if x == userog:
                    db.cou_user_32(1, x1)
                    await bot.send_message(message.from_user.id, 'Придется немного подождать.\nПроверяем расписание для студентов🧑‍🎓')

                    start =time.time()

                    try:
                        for i1 in ce():
                            if i1.find('студентов') >= 0:
                                await message.reply(shorten_url(i1), parse_mode='HTML')
                    except:
                        await message.reply('Ошибка')
                    end = time.time()
                    c = end - start
                    c1 = round(c, 2)
                    await bot.send_message(message.from_user.id, f'Время выполнение программы {c1} секунд')



@dp.message_handler(Text(equals='Расписание для преподавателей👨‍🏫'))
async def and_star12t(message: types.message, state: FSMContext):
    x = f'({str(message.chat.id)},)'

    x1 = x[1:-2]
    db.prepo(1, x1)
    vis = db.see_propod()
    masivich_1 = []
    for ib in vis:
        c = str(ib)
        c1 = c[1:-2]
        c2 = int(c1)
        masivich_1.append(c2)
    db.add_mas_prepod(sum(masivich_1))

    dec123 = CON(x1)
    for dec12 in dec123:
        dec_as = dec12[1:-2]

    if message.from_user.id == int(dec_as):
        for ITEG in con12(dec_as):
            global fr5
            fr5 = ITEG[1:-2]

            if len(fr5) >= 2:
                await bot.send_message(message.from_user.id, 'Слишком много попыток')
                await bot.send_message(message.from_user.id, f'Вы будете заблокированы на {30} секунд')
                prob = con12(x1)
                for dec in prob:
                    dec1 = dec[1:-2]
                    if int(dec1) >= 10:
                        await asyncio.sleep(20)
                        await dialog_4.whitelist.set()
                        db.cou_user_del(x1)
                        await state.finish()
                        await bot.send_message(message.from_user.id, f'Вы разблокированы')
                        db.cou_user_32(1, x1)

        else:
            for userog in BSD():
                if x == userog:
                    db.cou_user_32(1, x1)
                    start = time.time()
                    await bot.send_message(message.from_user.id, 'Придется немного подождать.\nПроверяем расписание для преподавателей.👨‍🏫')
                    try:
                        for i1 in ce():
                            if i1.find('преподавателей') >= 0:
                                await bot.send_message(message.from_user.id, shorten_url(i1), parse_mode='HTML')
                    except:
                        await message.reply('Ошибка')
                    end = time.time()
                    c = end - start
                    c1 = round(c, 2)
                    await bot.send_message(message.from_user.id, f'Время выполнение программы {c1} секунд')
                        # Сюда




@dp.message_handler(Text(equals='Кто создал'))
async def costar12t(message: types.message):
    await message.reply(qwerasfzv)


@dp.message_handler(Text(equals='Расписание звонков🔔'))
async def costar12t(message: types.message, state: FSMContext):
    x = f'({str(message.chat.id)},)'

    x1 = x[1:-2]

    dec123 = CON(x1)
    for dec12 in dec123:
        dec_as = dec12[1:-2]

    if message.from_user.id == int(dec_as):
        for ITEG in con12(dec_as):
            global fr4
            fr4 = ITEG[1:-2]

        if len(fr4) >= 2:
            await bot.send_message(message.from_user.id, 'Слишком много попыток')
            await bot.send_message(message.from_user.id, f'Вы будете заблокированы на {30} секунд')
            prob = con12(x1)
            for dec in prob:
                dec1 = dec[1:-2]
                if int(dec1) >= 10:
                    await asyncio.sleep(20)
                    await dialog_3.whitelist.set()
                    db.cou_user_del(x1)
                    await state.finish()
                    await bot.send_message(message.from_user.id, f'Вы разблокированы')
                    db.cou_user_32(1, x1)

        else:
            for userog in BSD():
                if x == userog:
                    db.cou_user_32(1, x1)
                    photo = open('rasp.jpg', 'rb')
                    photo_1 = open('rasp_sb.jpg', 'rb')
                    photo_2 = open('prk.jpg', 'rb')
                    await bot.send_photo(chat_id=message.chat.id, photo=photo)
                    await bot.send_photo(chat_id=message.chat.id, photo=photo_1)
                    await bot.send_photo(chat_id=message.chat.id, photo=photo_2)  # Сюда



@dp.message_handler(Text(equals='Ссылка на сайт'))
async def comand_t(message: types.message, state: FSMContext):
    x = f'({str(message.chat.id)},)'

    x1 = x[1:-2]
    dec123 = CON(x1)
    for dec12 in dec123:
        dec_as = dec12[1:-2]
        if message.from_user.id == int(dec_as):
            for ITEG in con12(x1):
                global fr3
                fr3 = ITEG[1:-2]

                if len(fr3) >= 2:
                    await bot.send_message(message.from_user.id, 'Слишком много попыток')
                    await bot.send_message(message.from_user.id, f'Вы будете заблокированы на {30} секунд')
                    prob = con12(x1)
                    for dec in prob:
                        dec1 = dec[1:-2]
                        if int(dec1) >= 10:
                            await asyncio.sleep(20)
                            await dialog_2.whitelist.set()
                            db.cou_user_del(x1)
                            await state.finish()
                            await bot.send_message(message.from_user.id, f'Вы разблокированы')
                            db.cou_user_32(1, x1)

                else:
                    for userog in BSD():
                        if x == userog:
                            db.cou_user_32(1, x1)

                            photo_log = open('logo.png', 'rb')
                            await bot.send_message(message.from_user.id,
                                       'https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html')
                            await bot.send_photo(chat_id=message.chat.id, photo=photo_log)  # Сюд


@dp.message_handler(Text(equals='рбк'))
async def comand_ar12t(message: types.message, state: FSMContext):
    x = f'({str(message.chat.id)},)'

    x1 = x[1:-2]

    dec123 = CON(x1)
    for dec12 in dec123:
        dec_as = dec12[1:-2]

    if message.from_user.id == int(dec_as):
        for ITEG in con12(dec_as):
            global fr2
            fr2 = ITEG[1:-2]

        if len(fr2) >= 2:
            await bot.send_message(message.from_user.id, 'Слишком много попыток')
            await bot.send_message(message.from_user.id, f'Вы будете заблокированы на {30} секунд')
            prob = con12(x1)
            for dec in prob:
                dec1 = dec[1:-2]
                if int(dec1) >= 10:
                    await asyncio.sleep(20)
                    await dialog1.whitelist.set()
                    db.cou_user_del(x1)
                    await state.finish()
                    await bot.send_message(message.from_user.id, f'Вы разблокированы')
                    db.cou_user_32(1, x1)

        else:
            for userog in BSD():
                if x == userog:
                    db.cou_user_32(1, x1)
                    await message.reply(parsing(), parse_mode='HTML')


@dp.message_handler(Text(equals='Дополнительное меню'))
async def comand_ar12t(message: types.message):
    if message.text == 'Дополнительное меню':
        await bot.send_message(message.from_user.id, 'Вы перешли в дополнительное меню', reply_markup=kb_client_1)

@dp.message_handler(Text(equals='Назад'))
async def comand_ar12t(message: types.message):

    if message.text == 'Назад':
        await bot.send_message(message.from_user.id, 'Вы перешли в основное меню', reply_markup=kb_client)



@dp.message_handler(Text(equals='Количество подписчиков'))
async def comand_ar12t(message: types.message):
    vis = db.see()
    masivich = []
    for ib in vis:
        c = str(ib)
        c1 = c[1:-2]
        c2 = int(c1)


        masivich.append(c2)




    await message.reply(f'Количество подписчиков: {len(masivich)}')





@dp.message_handler(Text(equals='id'))
async def user_id_inline_callback(message: types.message):
    await bot.send_message(message.from_user.id,f'{message.from_user.id} id' )



#@dp.message_handler(Text(equals='Удалить'))
#async def blabl1a(message: types.message):
#    db.cou_user_del_tim()
#    await bot.send_message(message.from_user.id, 'Все ходы удалены')



@dp.message_handler(Text(equals='Количество нажатий'))
async def blabl1(message: types.message):
    mas = []
    for se_Studen in db.see_stude_sume():
        c = str(se_Studen)
        c1 = c[1:-2]
        c2 = int(c1)
        mas.append(c2)
    await bot.send_message(message.from_user.id, f'Количество кликов на преподавателей: {mas[0]}')
    mas_1 = []
    for se_Studen_1 in db.see_prepod_sume():
        c_1 = str(se_Studen_1)
        c1_1 = c_1[1:-2]
        c2_1 = int(c1_1)
        mas_1.append(c2_1)
    await bot.send_message(message.from_user.id, f'Количество кликов на студентов: {mas_1[0]}')



@dp.message_handler(Text(equals='План мероприятий'))
async def blabl1a(message: types.message, state: FSMContext):
    x = f'({str(message.chat.id)},)'

    x1 = x[1:-2]


    dec123 = CON(x1)
    for dec12 in dec123:
        dec_as = dec12[1:-2]



    if message.from_user.id == int(dec_as):
        for ITEG in con12(dec_as):
            global fr12

            fr12 = ITEG[1:-2]




        if int(fr12) >= 10:
            await bot.send_message(message.from_user.id, 'Слишком много попыток')
            await bot.send_message(message.from_user.id, f'Вы будете заблокированы на {30} секунд')
            prob = con12(x1)
            for dec in prob:
                dec1 = dec[1:-2]
                if int(dec1) >= 10:
                        await asyncio.sleep(20)
                        await dialog8.whitelist.set()
                        db.cou_user_del(x1)
                        await state.finish()
                        await bot.send_message(message.from_user.id, f'Вы разблокированы')
                        db.cou_user_32(1, x1)
        else:
            for userog in BSD():
                if x == userog:
                    db.cou_user_32(1, x1)
                    await bot.send_message(message.from_user.id, 'Придется немного подождать...')
                    try:
                        await bot.send_message(message.from_user.id, shorten_url(parsing_odd_1221()), parse_mode='HTML')
                    except:
                        await message.reply('Ошибка')






@dp.message_handler(Text(equals='1'))
async def blabl1a(message: types.message, state: FSMContext):
    x = f'({str(message.chat.id)},)'

    x1 = x[1:-2]


    dec123 = CON(x1)
    for dec12 in dec123:
        dec_as = dec12[1:-2]



    if message.from_user.id == int(dec_as):
        for ITEG in con12(dec_as):
            global fr1

            fr1 = ITEG[1:-2]




        if int(fr1) >= 10:
            await bot.send_message(message.from_user.id, 'Слишком много попыток')
            await bot.send_message(message.from_user.id, f'Вы будете заблокированы на {30} секунд')
            prob = con12(x1)
            for dec in prob:
                dec1 = dec[1:-2]
                if int(dec1) >= 10:
                        await asyncio.sleep(20)
                        await dialog.whitelist.set()
                        db.cou_user_del(x1)
                        await state.finish()
                        await bot.send_message(message.from_user.id, f'Вы разблокированы')
                        db.cou_user_32(1, x1)
        else:
            for userog in BSD():
                if x == userog:
                    db.cou_user_32(1, x1)
                    await message.reply('Успех')







executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
