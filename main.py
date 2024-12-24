from dotenv import dotenv_values
from storage import StorageUsers, StorageContent
from user import User
from telebot import TeleBot, types
from view import Text, Image, View

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = TeleBot(TOKEN)
stg_users = StorageUsers()
stg_content = StorageContent.create()
vw = View(bot)


@bot.message_handler(commands=['start'])
def start(message):
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
    vw.send(message.chat.id, stg_content, 'start', user.lang)


bot.polling(none_stop=True)
