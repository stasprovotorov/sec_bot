from dotenv import dotenv_values
from storage import StorageUsers, StorageContent
from user import User, Language
from telebot import TeleBot, types
from view import Text, Image, View

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']


bot = TeleBot(TOKEN)
stg_users = StorageUsers()
stg_content = StorageContent()
vw = View(bot, stg_content)


@bot.message_handler(commands=['start'])
def start(message):
    content_key = message.text.lstrip('/')
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
    vw.send(message.chat.id, content_key, user.lang)

@bot.callback_query_handler(func=lambda call: True)
def buttons_callback(call):
    content_key = call.data
    user = User(stg_users, call.message.from_user.id, call.message.from_user.language_code)
    vw.send(call.message.chat.id, content_key, user.lang)


bot.polling(none_stop=True)
