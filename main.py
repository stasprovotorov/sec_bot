from dotenv import load_dotenv
from os import getenv
import telebot

load_dotenv('tg_bot_token.env')
TOKEN = getenv('TOKEN')
bot_lang = 'en'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    global bot_lang
    user_lang = message.from_user.language_code
    bot_lang = user_lang
    message_back = {
        'en': 'Welcome! Your language is set to English',
        'ru': 'Добро пожаловать! Ваш язык установлен на русский'
        }
    bot.send_message(message.chat.id, message_back[user_lang])


bot.polling(none_stop=True)
