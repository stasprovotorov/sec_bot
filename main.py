from dotenv import dotenv_values
from telebot import TeleBot, types
from objs import Users, User
import messages as msg

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = TeleBot(TOKEN)
users = Users()


@bot.message_handler(commands=['start'])
def start(message):
    pass


bot.polling(none_stop=True)
