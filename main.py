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
    id = str(message.from_user.id)
    if id not in users:
        lang = 'ru' if message.from_user.language_code == 'ru' else 'en'
        users[id] = User(lang)
    else:
        lang = users[id].language
    keyboard = types.InlineKeyboardMarkup()
    change_lang_btn = types.InlineKeyboardButton(msg.change_lang_btn[lang], callback_data='change_language')
    keyboard.add(change_lang_btn)
    bot.send_message(message.chat.id, msg.start[lang], reply_markup=keyboard)


bot.polling(none_stop=True)
