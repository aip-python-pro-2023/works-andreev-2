import os
import telebot
from telebot import types, custom_filters
from telebot.formatting import escape_markdown
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv
from telebot.types import InlineKeyboardButton, ReplyKeyboardRemove

from ingredient import Ingredient, IngredientsRepository

load_dotenv()
state_storage = StateMemoryStorage()


TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_TOKEN, state_storage=state_storage)

ingredients_repository = IngredientsRepository()


class SearchStates(StatesGroup):
    search_ingredient = State()
    search_recipe = State()


class CreateIngredientStates(StatesGroup):
    add_name = State()
    add_description = State()
    add_type = State()
    add_picture = State()
    add_numbers = State()
    confirm = State()


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


@bot.message_handler(commands=['add_ingredient'])
def start_add_ingredient(message: types.Message):
    response = 'Введите название ингредиента'
    bot.set_state(message.from_user.id, CreateIngredientStates.add_name)
    bot.send_message(message.chat.id, escape_markdown(response), parse_mode='MarkdownV2')


@bot.message_handler(state=CreateIngredientStates.add_name)
def add_ingredient_name(message: types.Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    response = 'Введите описание ингредиента'
    bot.set_state(message.from_user.id, CreateIngredientStates.add_description)
    bot.send_message(message.chat.id, escape_markdown(response), parse_mode='MarkdownV2')


@bot.message_handler(state=CreateIngredientStates.add_description)
def add_ingredient_description(message: types.Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['description'] = message.text
    response = 'Выберите тип ингредиента'
    bot.set_state(message.from_user.id, CreateIngredientStates.add_type)
    bot.send_message(message.chat.id, escape_markdown(response), parse_mode='MarkdownV2')


@bot.message_handler(state=CreateIngredientStates.add_type)
def add_ingredient_type(message: types.Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['ingredient_type'] = message.text
    response = 'Вставьте ссылку на картинку'
    bot.set_state(message.from_user.id, CreateIngredientStates.add_picture)
    bot.send_message(message.chat.id, escape_markdown(response), parse_mode='MarkdownV2')


@bot.message_handler(state=CreateIngredientStates.add_picture)
def add_ingredient_picture(message: types.Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['picture'] = message.text
    response = 'Введите КБЖУ в формате К/Б/Ж/У'
    bot.set_state(message.from_user.id, CreateIngredientStates.add_numbers)
    bot.send_message(message.chat.id, escape_markdown(response), parse_mode='MarkdownV2')


@bot.message_handler(state=CreateIngredientStates.add_numbers)
def add_ingredient_numbers(message: types.Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        calories, proteins, fats, carbohydrates = [int(x) for x in message.text.split('/')]
        data['calories'] = calories
        data['proteins'] = proteins
        data['fats'] = fats
        data['carbohydrates'] = carbohydrates

        response = f'''Добавить этот ингредиент?
Название: {data['name']}
Описание: {data['description']}
Тип: {data['ingredient_type']}
Картинка: {data['picture']}
Калории: {data['calories']}
Белки: {data['proteins']}
Жиры: {data['fats']}
Углеводы: {data['carbohydrates']}
'''
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row(
        telebot.types.KeyboardButton('Да'),
        telebot.types.KeyboardButton('Нет')
    )
    bot.set_state(message.from_user.id, CreateIngredientStates.confirm)
    bot.send_message(message.chat.id, escape_markdown(response), parse_mode='MarkdownV2', reply_markup=markup)


@bot.message_handler(state=CreateIngredientStates.confirm, regexp='Да')
def add_ingredient_save(message: types.Message):
    response = 'Ингредиент успешно добавлен!'
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        ingredients_repository.save(Ingredient(**data))
    bot.delete_state(message.chat.id)
    bot.send_message(message.chat.id,
                     escape_markdown(response),
                     parse_mode='MarkdownV2',
                     reply_markup=ReplyKeyboardRemove())


@bot.message_handler(state=CreateIngredientStates.confirm, regexp='Нет')
def add_ingredient_reset(message: types.Message):
    response = 'Ингредиент не был добавлен'
    bot.delete_state(message.chat.id)
    bot.send_message(message.chat.id,
                     escape_markdown(response),
                     parse_mode='MarkdownV2',
                     reply_markup=ReplyKeyboardRemove())


@bot.message_handler(func=lambda m: True)
def echo_all(message: types.Message):
    bot.reply_to(message, 'Непонятное сообщение :(')
    send_help(message)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.infinity_polling()
