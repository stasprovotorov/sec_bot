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
    ask_button_name = State()
    ask_content_key = State()
    ask_label_ru = State()
    ask_label_en = State()
    ask_content_key_back = State()

    button_name = None
    content_key = None
    label_ru = None
    label_en = None
    content_key_back = None

@bot.message_handler(commands=['start'])
def start(message):
    content_key = message.text.lstrip('/')
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
    is_admin = stg_users.is_admin(user.user_id)
    # is_admin = not stg_users.is_admin(user.user_id)
    vw.send(message.chat.id, content_key, user.lang, is_admin)


@bot.callback_query_handler(func=lambda call: call.data == 'edit')
def edit(call):
    msg = 'Hello! What you want to edit?'
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('Create Button', callback_data='create_button'))
    bot.send_message(call.message.chat.id, msg, reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'create_button')
def ask_button_name(call):
    msg = 'Enter the button_name'
    bot.send_message(call.from_user.id, msg)
    bot.set_state(call.from_user.id, EditorStates.ask_button_name, call.message.chat.id)


@bot.message_handler(state=EditorStates.ask_button_name, content_types=['text'])
def get_button_name(message):
    EditorStates.button_name = message.text
    print(f'Button name set to: {EditorStates.button_name}')
    bot.send_message(message.from_user.id, 'Enter content_key')
    bot.set_state(message.from_user.id, EditorStates.ask_content_key, message.chat.id)


@bot.message_handler(state=EditorStates.ask_content_key, content_types=['text'])
def get_button_content_key(message):
    EditorStates.content_key = message.text
    print(f'Button content_key set to: {EditorStates.content_key}')
    bot.send_message(message.from_user.id, 'Enter button label_ru')
    bot.set_state(message.from_user.id, EditorStates.ask_label_ru, message.chat.id)

@bot.message_handler(state=EditorStates.ask_label_ru, content_types=['text'])
def get_button_label_ru(message):
    EditorStates.label_ru = message.text
    print(f'Button label_ru set to: {EditorStates.label_ru}')
    bot.send_message(message.from_user.id, 'Enter button label_en')
    bot.set_state(message.from_user.id, EditorStates.ask_label_en, message.chat.id)


@bot.message_handler(state=EditorStates.ask_label_en, content_types=['text'])
def get_button_label_en(message):
    EditorStates.label_en = message.text
    print(f'Button label_en set to: {EditorStates.label_en}')
    bot.send_message(message.from_user.id, 'Enter content_key_back')
    bot.set_state(message.from_user.id, EditorStates.ask_content_key_back, message.chat.id)


@bot.message_handler(state=EditorStates.ask_content_key_back, content_types=['text'])
def get_button_content_key_back(message):
    EditorStates.content_key_back = message.text
    print(f'Button content_key_back set to: {EditorStates.content_key_back}')
    stg_content.save_button(
        EditorStates.button_name,
        Language.RU,
        EditorStates.label_ru,
        EditorStates.content_key_back
    )
    stg_content.save_button(
        EditorStates.button_name,
        Language.EN,
        EditorStates.label_en,
        EditorStates.content_key_back
    )


@bot.callback_query_handler(func=lambda call: call.data != 'create_button')
def buttons_callback(call):
    content_key = call.data
    user = User(stg_users, call.message.from_user.id, call.message.from_user.language_code)
    is_admin = stg_users.is_admin(user.user_id)
    # is_admin = not stg_users.is_admin(user.user_id)
    vw.send(call.message.chat.id, content_key, user.lang, is_admin)


bot.polling(none_stop=True)
