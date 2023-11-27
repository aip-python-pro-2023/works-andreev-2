import os
import telebot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = 'Привет\\! Это бот с кулинарной книгой и поиску по рецептам\\. Для помощи отправь /help'
    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(commands=['help'])
def send_help(message):
    response = """Основные команды:

/recipe \\- найти рецепт по названию и/или по ингредиентам
/ingredient \\- найти ингредиент по названию и все рецепты с ним
/favourite \\- открыть список избранных рецептов

В каждой команде есть управление кнопками
"""
    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, 'Непонятное сообщение :(')
    send_help(message)


bot.infinity_polling()
