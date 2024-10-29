from dotenv import dotenv_values
import telebot
from objs import Users, User

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = telebot.TeleBot(TOKEN)
users = Users()


@bot.message_handler(commands=['start'])
def start(message):
    id = str(message.from_user.id)
    language = message.from_user.language_code
    if id not in users:
        users[id] = User(language)
    else:
        language = users[id].language
    message_back = {
        'en': 'Welcome! Your language is set to English',
        'ru': 'Добро пожаловать! Для вас установлен русский язык'
        }
    bot.send_message(message.chat.id, message_back[language])


bot.polling(none_stop=True)
