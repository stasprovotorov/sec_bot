from dotenv import dotenv_values
from storage import StorageUsers, StorageContent
from user import User, Language
from telebot import TeleBot, types
from view import Text, Image, View

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']


bot = TeleBot(TOKEN)
stg_users = StorageUsers()
stg_content = StorageContent.create()
vw = View(bot, stg_content)
content_key = 'start'
user_lang = Language.EN
text = vw.get_text(content_key, user_lang) 

print(text)

# @bot.message_handler(commands=['start'])
# def start(message):
#     pass


# @bot.callback_query_handler(func=lambda call: True)
# def buttons_callback(call):
#     pass

# bot.polling(none_stop=True)

