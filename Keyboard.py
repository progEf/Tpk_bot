from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


b1 = KeyboardButton('Расписание для студентов🧑‍🎓')
b2 = KeyboardButton('Ссылка на сайт')
b3 = KeyboardButton('Расписание для преподавателей👨‍🏫')
b4 = KeyboardButton('Расписание звонков🔔')
b5 = KeyboardButton('рбк')
b6 = KeyboardButton('Дополнительное меню')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b3).row(b4, b2).add(b6)

b4_1 = KeyboardButton('План мероприятий')
b5_1 = KeyboardButton('Количество подписчиков')
b6_1 = KeyboardButton('Количество нажатий')
b7_1 = KeyboardButton('Назад')
kb_client_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_1.add(b4_1).row(b5_1, b6_1).add(b7_1)