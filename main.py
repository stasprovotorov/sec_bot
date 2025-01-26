from dotenv import dotenv_values
from storage import StorageUsers, StorageContent
from user import User
from telebot import TeleBot, types, custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from view import View

from editor import Editor, StatesButton, StatesText
from editor_data import editor_msg, editor_btn

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

storage = StateMemoryStorage()
bot = TeleBot(TOKEN, state_storage=storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))

stg_users = StorageUsers()
stg_content = StorageContent()
stg_content.lazy_init()
vw = View(bot, stg_content)

editor = Editor()


@bot.message_handler(commands=['start'])
def start(message):
    user = User(stg_users, message.from_user.id+1, message.from_user.language_code)
    view = message.text.lstrip('/')
    vw.send(message.chat.id, view, user.lang, user.role)


@bot.callback_query_handler(func=lambda call: call.data == 'editor_menu')
def editor_menu(call):
    msg = editor_msg[call.data][call.from_user.language_code]
    btn_row = []
    row_width = 2
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    for i, btn_name in enumerate(editor_btn[call.data], start=1):
        btn_row.append(
            types.InlineKeyboardButton(
                text=editor_btn[call.data][btn_name]['label'][call.from_user.language_code],
                callback_data=editor_btn[call.data][btn_name]['cnt_next']
            )
        )
        if i % row_width == 0:
            keyboard.row(*btn_row)
            btn_row.clear()
    bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'edit_txt_menu')
def edit_txt_menu(call):
    msg = editor_msg[call.data][call.from_user.language_code]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    btn_row = []
    for btn_name in editor_btn[call.data]:
        btn_row.append(
            types.InlineKeyboardButton(
                text=editor_btn[call.data][btn_name]['label'][call.from_user.language_code],
                callback_data=editor_btn[call.data][btn_name]['cnt_next']
            )
        )
    keyboard.row(*btn_row)
    bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'text_sys_name')
def new_txt(call):
    msg = editor_msg[call.data][call.from_user.language_code]
    bot.set_state(call.from_user.id, StatesText.text_ru, call.message.chat.id)
    bot.send_message(call.from_user.id, msg)


@bot.message_handler(state=StatesText.get_states_obj(), content_types=['text'])
def new_txt_dialog(message):
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
    user.lang = 'en' # fix it
    user_state = bot.get_state(message.from_user.id)
    chat_id = message.chat.id
    user_input = message.text
    editor.dialog_provider(bot, user, user_state, chat_id, user_input)


@bot.callback_query_handler(func=lambda call: call.data in ['confirm', 'cancel'])
def confirmation(call):
    if call.data == 'confirm':
        content_type ='text' if editor.dialog_data.keys()[0].split(':')[0] == 'StatesText' else None
        print(content_type)
    elif call.data == 'cancel':
        editor.dialog_data.clear()
    print(editor.dialog_data)


@bot.callback_query_handler(func=lambda call: call.data != 'create_button')
def buttons_callback(call):
    content_key = call.data
    user = User(stg_users, call.message.from_user.id, call.message.from_user.language_code)
    is_admin = stg_users.is_admin(user.user_id)
    # is_admin = not stg_users.is_admin(user.user_id)
    vw.send(call.message.chat.id, content_key, user.lang, is_admin)


bot.polling(none_stop=True)
