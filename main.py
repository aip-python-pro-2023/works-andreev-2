import os
import telebot
from telebot import types, custom_filters
from telebot.formatting import escape_markdown
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv

from ingredient import Ingredient, IngredientsRepository

load_dotenv()
state_storage = StateMemoryStorage()


TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_TOKEN, state_storage=state_storage)

ingredients_repository = IngredientsRepository()


class SearchStates(StatesGroup):
    search_ingredient = State()
    search_recipe = State()


@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    response = 'Привет\\! Это бот с кулинарной книгой и поиску по рецептам\\. Для помощи отправь /help'
    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(commands=['help'])
def send_help(message: types.Message):
    response = """Основные команды:

/recipe \\- найти рецепт по названию и/или по ингредиентам
/ingredient \\- найти ингредиент по названию и все рецепты с ним
/favourite \\- открыть список избранных рецептов

В каждой команде есть управление кнопками
"""
    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(commands=['ingredient'])
def search_ingredients(message: types.Message):
    response = 'Введите название ингредиента или его часть'
    bot.set_state(message.from_user.id, SearchStates.search_ingredient)
    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2')


@bot.message_handler(state=SearchStates.search_ingredient)
def search_ingredient(message: types.Message):
    result = ingredients_repository.find(message.text)
    if result:
        response = str(result[0])
    else:
        response = f'Ингредиенты с названием {message.text} не найдены'
    bot.delete_state(message.from_user.id)
    bot.send_message(message.chat.id, escape_markdown(response), parse_mode='MarkdownV2')


@bot.message_handler(func=lambda m: True)
def echo_all(message: types.Message):
    bot.reply_to(message, 'Непонятное сообщение :(')
    send_help(message)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.infinity_polling()
