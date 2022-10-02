import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot('5712366693:AAFlQ-NFnYchZfnZy6pXq89IGPQcCemFCsE')

"""@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id,
                     f'Текущая дата {datetime.today().strftime("%d.%m.%Y")}')
"""


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Расписание")
    markup.add(button1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я подскажу "
                          "расписание.".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Расписание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        today_button = types.KeyboardButton("На сегодня")
        tomorrow_button = types.KeyboardButton("На завтра")
        date_button = types.KeyboardButton("На определенную дату")
        markup.add(today_button, tomorrow_button, date_button)
        bot.send_message(message.chat.id,
                         text="На какой день нужно "
                              "расписание?".format(message.from_user),
                         reply_markup=markup)

    elif message.text == "На сегодня":
        bot.send_message(message.chat.id,
                         text="Сегодня...")

    elif message.text == "На завтра":
        bot.send_message(message.chat.id,
                         text="Завтра...")

    elif message.text == "На определенную дату":
        bot.send_message(message.chat.id,
                         text="Укажи дату")

    else:
        bot.send_message(message.chat.id,
                         text="На такую комманду я не запрограммирован..")


bot.polling(none_stop=True, interval=0)
