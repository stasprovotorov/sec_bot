from dotenv import dotenv_values
from storage import StorageUsers, StorageKeyboard
from user import User
from telebot import TeleBot
from view import Text, Image, View

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = TeleBot(TOKEN)
stg_users = StorageUsers()
stg_keyboard = StorageKeyboard()


@bot.message_handler(commands=['start'])
def start(message):
    user = User(
        stg_users, 
        message.from_user.id, 
        message.from_user.language_code
    )
    text = Text('Добро пожаловать!', 'Welcome!')
    keyboard = stg_keyboard.get_keyboard('start')
    bot.send_message(
        message.chat.id, 
        text.content[user.lang], 
        reply_markup=keyboard(user.lang)
    )
    user.switch_lang()


bot.polling(none_stop=True)
