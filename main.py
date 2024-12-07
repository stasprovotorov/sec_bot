from dotenv import dotenv_values
from storage import StorageUsers
from user import User
from telebot import TeleBot
from view import Text, Image, View

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = TeleBot(TOKEN)
users_db = StorageUsers()


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    lang = message.from_user.language_code
    user = User(users_db, user_id, lang)
    text = Text('Привет!', 'Hello!')
    img = Image('sec_poster.jpg')
    view = View(bot, user, text, img)
    view.send()


bot.polling(none_stop=True)
