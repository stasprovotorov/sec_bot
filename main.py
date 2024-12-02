from dotenv import dotenv_values
from storage import StorageUsers
from user import User
from telebot import TeleBot

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = TeleBot(TOKEN)
users_db = StorageUsers()


@bot.message_handler(commands=['start'])
def start(message):
    pass
    # user = User(users_db, message.chat.id, message.from_user.language_code)
    # users_db.save_user(user)


bot.polling(none_stop=True)
