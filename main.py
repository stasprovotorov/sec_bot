from dotenv import dotenv_values
from storage import StorageUsers
from user import User
from telebot import TeleBot
from message import Text, Message

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = TeleBot(TOKEN)
users_db = StorageUsers()


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    lang = message.from_user.language_code
    user = User(users_db, user_id, lang)


bot.polling(none_stop=True)
