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


@bot.callback_query_handler(func=lambda call: call.data == 'change_language')
def change_language(call):
    id = str(call.from_user.id)
    lang = 'ru' if users[id].language == 'en' else 'en'
    users[id] = User(lang)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Button 1', callback_data='button_1'))
    keyboard.add(types.InlineKeyboardButton('Button 2', callback_data='button_2'))
    keyboard.add(types.InlineKeyboardButton('Button 3', callback_data='button_3'))
    keyboard.add(types.InlineKeyboardButton('Button 4', callback_data='button_4'))
    bot.send_message(
        call.message.chat.id, 
        msg.changed_lang[users[id].language],
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == 'button_1')
def button_1(call):
    bot.send_message(call.message.chat.id, 'Command 1 executed')


@bot.callback_query_handler(func=lambda call: call.data == 'button_2')
def button_1(call):
    bot.send_message(call.message.chat.id, 'Command 2 executed')


@bot.callback_query_handler(func=lambda call: call.data == 'button_3')
def button_1(call):
    bot.send_message(call.message.chat.id, 'Command 3 executed')


@bot.callback_query_handler(func=lambda call: call.data == 'button_4')
def button_1(call):
    bot.send_message(call.message.chat.id, 'Command 4 executed')


bot.polling(none_stop=True)
