from dotenv import dotenv_values
from storage import StorageUsers, StorageContent
from user import User
from telebot import TeleBot, types, custom_filters
from telebot.storage import StateMemoryStorage
from view import View

from editor import Editor
from editor_data import editor_msg, editor_btn, state_group_to_content_type

config = dotenv_values('tg_bot_token.env')
TOKEN = config['TOKEN']

storage = StateMemoryStorage()
bot = TeleBot(TOKEN, state_storage=storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))

stg_users = StorageUsers()
stg_content = StorageContent()
stg_content.lazy_init()

vw = View(bot, stg_content)

editor = Editor(stg_content)


@bot.message_handler(commands=['start'])
def start(message):
    user = User(stg_users, message.from_user.id, message.from_user.language_code)
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


@bot.callback_query_handler(func=lambda call: call.data.startswith('state'))
def start_editor_dialog(call):
    user = User(stg_users, call.from_user.id, call.from_user.language_code)

    _, state_category, state_group = call.data.split(':')
    states_iter = editor.states[state_category][state_group].get_states_iter()
    editor.set_user_states(user.id, states_iter)
    user_state = editor.get_next_user_state(user.id)
    bot.set_state(user.id, user_state)

    _, _, state_name = editor.state_parser(user_state)

    msg = editor_msg[state_category][state_group][state_name][user.lang]
    keyboard = editor.state_to_keyboard(state_name)

    bot.send_message(user.id, msg, reply_markup=keyboard)


@bot.message_handler(state=editor.get_all_states(), content_types=['text'])
def editor_dialog_provider(message):
    user = User(stg_users, message.from_user.id, message.from_user.language_code)

    editor.collect_user_responses(
        user_id=user.id,
        user_state=bot.get_state(user.id), 
        user_input=message.text
    )
    
    try:
        state = editor.get_next_user_state(user.id)

        bot.set_state(user.id, state)

        content_type, action, state_name = editor.state_parser(state)

        keyboard = editor.state_to_keyboard(state_name)
        msg = editor_msg[content_type][action][state_name][user.lang]

        bot.send_message(user.id, msg, reply_markup=keyboard)

    except StopIteration:
        bot.delete_state(user.id)

        msg = editor_msg['confirmation']['confirm_request'][user.lang]

        keyboard = types.InlineKeyboardMarkup()
        buttons = []
        for button_name in editor_btn['confirmation']:
            buttons.append(
                types.InlineKeyboardButton(
                    text=editor_btn['confirmation'][button_name]['label'][user.lang],
                    callback_data=editor_btn['confirmation'][button_name]['cnt_next']
                )
            )
        keyboard.row(*buttons)

        bot.send_message(user.id, msg, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ['confirm', 'cancel'])
def confirmation(call):
    user = User(stg_users, call.from_user.id, call.from_user.language_code)

    if call.data == 'confirm':
        editor.commit_user_responses(
            content_type=editor.user_responses[user.id]['content_type'],
            action=editor.user_responses[user.id]['action'],
            user_responses=editor.user_responses[user.id]['user_responses']
        )

        editor.user_responses[user.id].clear()

        msg = editor_msg['confirmation']['confirm_response']['approved'][user.lang]
        bot.send_message(user.id, msg)

    elif call.data == 'cancel':
        editor.user_responses[user.id].clear()

        msg = editor_msg['confirmation']['confirm_response']['canceled'][user.lang]
        bot.send_message(user.id, msg)


@bot.callback_query_handler(func=lambda call: call.data != 'create_button')
def buttons_callback(call):
    view = call.data
    user = User(stg_users, call.from_user.id, call.from_user.language_code)
    vw.send(call.message.chat.id, view, user.lang)


bot.polling(none_stop=True)
