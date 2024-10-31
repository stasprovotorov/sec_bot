from dotenv import dotenv_values
import telebot
from objs import Users, User
import messages as msg

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

bot = telebot.TeleBot(TOKEN)
users = Users()


@bot.message_handler(commands=['start'])
def start(message):
    id = str(message.from_user.id)
    if id not in users:
        language = 'ru' if message.from_user.language_code == 'ru' else 'en'
        users[id] = User(language)
    else:
        language = users[id].language
    bot.send_message(message.chat.id, msg.start[language])


bot.polling(none_stop=True)
