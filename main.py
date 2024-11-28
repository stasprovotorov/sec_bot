from dotenv import dotenv_values
from storage import StorageUsers
from user import User
from telebot import TeleBot

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = TeleBot(TOKEN)
su = StorageUsers()


@bot.message_handler(commands=['start'])
def start(message):
    user_obj = User(message.from_user.id, message.from_user.language_code)
    su.save_user(user_obj.id, user_obj)


bot.polling(none_stop=True)
