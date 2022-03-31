import telebot
import os
import datetime


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


bot = telebot.TeleBot('5260289062:AAEWp6Fprpntic54jD9b9TFRB2jSEAt34uQ')

@bot.message_handler(commands=['start'])
def blablamethod(message):
    if os.stat(f"36&6_{date}.csv").st_size == 0:
        bot.send_message(message.chat.id, "366 is empty")

bot.infinity_polling()
