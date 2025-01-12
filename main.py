from dotenv import dotenv_values
from storage import StorageUsers, StorageContent
from user import User, Language
from telebot import TeleBot, types, custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from view import Text, Image, View

from editor import Editor, StatesButton, editor_dialog

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

storage = StateMemoryStorage()
bot = TeleBot(TOKEN, state_storage=storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))

stg_users = StorageUsers()
stg_content = StorageContent()
vw = View(bot, stg_content)

editor = Editor()

@bot.message_handler(commands=['start'])
def start(message):
    content_key = message.text.lstrip('/')
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
    user.switch_lang()
    is_admin = stg_users.is_admin(user.user_id)
    # is_admin = not stg_users.is_admin(user.user_id)
    vw.send(message.chat.id, content_key, user.lang, is_admin)


@bot.callback_query_handler(func=lambda call: call.data == 'edit')
def edit(call):
    user = User(stg_users, call.from_user.id, call.from_user.language_code)
    message = editor_dialog[call.data][user.lang]
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('Create Button', callback_data='create_button'))
    bot.send_message(call.message.chat.id, message, reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'create_button')
def start_create_button(call):
    user = User(stg_users, call.from_user.id, call.from_user.language_code)
    bot.set_state(call.from_user.id, StatesButton.btn_sys_name, call.message.chat.id)
    state_key, question_key = bot.get_state(user.user_id).split(':')
    bot.send_message(user.user_id, editor_dialog[state_key][question_key][user.lang])


@bot.message_handler(state=StatesButton.get_states_obj(), content_types=['text'])
def dialog_create_button(message):
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
    user_state = bot.get_state(message.from_user.id)
    chat_id = message.chat.id
    editor.dialog_provider(bot, user, user_state, chat_id)


@bot.callback_query_handler(func=lambda call: call.data != 'create_button')
def buttons_callback(call):
    content_key = call.data
    user = User(stg_users, call.message.from_user.id, call.message.from_user.language_code)
    is_admin = stg_users.is_admin(user.user_id)
    # is_admin = not stg_users.is_admin(user.user_id)
    vw.send(call.message.chat.id, content_key, user.lang, is_admin)


bot.polling(none_stop=True)
