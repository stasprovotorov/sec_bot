from dotenv import dotenv_values
from storage import StorageUsers, StorageContent
from user import User, Language
from telebot import TeleBot, types, custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from view import Text, Image, View

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

storage = StateMemoryStorage()
bot = TeleBot(TOKEN, state_storage=storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))

stg_users = StorageUsers()
stg_content = StorageContent()
vw = View(bot, stg_content)


class EditorStates(StatesGroup):
    state_text = State()


@bot.message_handler(commands=['start'])
def start(message):
    content_key = message.text.lstrip('/')
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
    is_admin = stg_users.is_admin(user.user_id)
    # is_admin = not stg_users.is_admin(user.user_id)
    vw.send(message.chat.id, content_key, user.lang, is_admin)


@bot.callback_query_handler(func=lambda call: call.data == 'edit')
def edit(call):
    bot.set_state(call.from_user.id, EditorStates.state_text, call.message.chat.id)
    bot.send_message(call.message.chat.id, 'Type text, please!')


@bot.message_handler(state=EditorStates.state_text, content_types=['text'])
def get_text_from_user(message):
    print(message.text)
    bot.delete_state(message.from_user.id)


@bot.callback_query_handler(func=lambda call: call.data != 'edit')
def buttons_callback(call):
    content_key = call.data
    user = User(stg_users, call.message.from_user.id, call.message.from_user.language_code)
    is_admin = stg_users.is_admin(user.user_id)
    # is_admin = not stg_users.is_admin(user.user_id)
    vw.send(call.message.chat.id, content_key, user.lang, is_admin)


bot.polling(none_stop=True)
