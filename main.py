from dotenv import load_dotenv
from os import getenv
import telebot

load_dotenv('tg_bot_token.env')
TOKEN = getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    print(message.from_user)
    bot.send_message(message.chat.id, '❤️ Анечка ❤️')


bot.polling(none_stop=True)
