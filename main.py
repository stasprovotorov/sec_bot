from dotenv import dotenv_values
from telebot.storage import StateMemoryStorage

from storage import StorageUsers, StorageContent
from user import User
from telebot import TeleBot, types
from view import View
from editor import Editor, StatesViewEdit
from editor_data import editor_msg, editor_btn, state_group_to_content_type

# Load the Telegram bot token from config.env
config = dotenv_values('config.env')
TELEGRAM_BOT_TOKEN = config['TELEGRAM_BOT_TOKEN']

# Initialize the Telegram bot object with a StateMemoryStorage object for storing user states
state_storage = StateMemoryStorage()
bot = TeleBot(TELEGRAM_BOT_TOKEN, state_storage=state_storage)

stg_users = StorageUsers()
stg_content = StorageContent()
stg_content.lazy_init()

vw = View(bot, stg_content)

editor = Editor(stg_content)

call_filter = {
    'editor_view_component_action': (
        'editor_view_action_text',
        'editor_view_action_image',
        'editor_view_action_button'
    )
}

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


@bot.callback_query_handler(func=lambda call: call.data in ['edit_txt_menu', 'edit_img_menu', 'edit_btn_menu', 'edit_vw_menu'])
def edit_content_type_menu(call):
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


@bot.callback_query_handler(func=lambda call: call.data == 'editor_view_component_choice')
def editor_view_component_choice(call):
    user = User(stg_users, call.from_user.id, call.from_user.language_code)
    callback_data = call.data

    message = editor_msg[callback_data][user.lang]

    buttons = []
    for button_name in editor_btn[callback_data]:
        buttons.append(
            types.InlineKeyboardButton(
                text=editor_btn[callback_data][button_name]['label'][user.lang],
                callback_data=editor_btn[callback_data][button_name]['callback_data']
            )
        )

    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*buttons)

    bot.send_message(user.id, message, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('editor_view_component'))
def editor_view_name_choice(call):
    user = User(stg_users, call.from_user.id, call.from_user.language_code)

    _, view_component = call.data.split(':')
    
    editor.save_user_input(user.id, view_component=view_component)

    bot.set_state(user.id, StatesViewEdit.push_view_name)
    _, state = StatesViewEdit.push_view_name.name.split(':')

    keyboard = editor.state_to_keyboard(state)

    bot.send_message(
        user.id,
        text=editor_msg['view']['edit'][state][user.lang],
        reply_markup=keyboard
    )


# @bot.callback_query_handler(func=lambda call: call.data.startswith('editor_view_action'))
# def editor_view_component_action(call):
#     user = User(stg_users, call.from_user.id, call.from_user.language_code)
#     callback_data, view_component = call.data.split(':')

#     editor.collect_user_input(user_id=user.id, view_component=view_component)

#     message = editor_msg[callback_data][user.lang]

#     buttons = []
#     for button_name in editor_btn['editor_view_action']:
#         buttons.append(
#             types.InlineKeyboardButton(
#                 text=editor_btn['editor_view_action'][button_name]['label'][user.lang],
#                 callback_data=editor_btn['editor_view_action'][button_name]['callback_data']
#             )
#         )

#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.row(*buttons)

#     bot.send_message(user.id, message, reply_markup=keyboard)


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


@bot.message_handler(state=editor.get_all_states(), content_types=['text', 'photo'])
def editor_dialog_provider(message):
    user = User(stg_users, message.from_user.id, message.from_user.language_code)

    state = bot.get_state(user.id)

    if message.text:
        user_input = message.text

        if state in editor.multi_push_state and message.text != 'Commit selection':
            editor.user_multi_push_data.append(user_input)

            return
        
        elif state in editor.multi_push_state and message.text == 'Commit selection':
            user_input = editor.user_multi_push_data

    elif message.photo:
        image_id = message.photo[-1].file_id
        image_info = bot.get_file(image_id)
        image = bot.download_file(image_info.file_path)
        
        user_input = image

    editor.collect_user_input(
        user_id=user.id,
        user_input=user_input,
        user_state=bot.get_state(user.id)
    )
    
    try:
        state = editor.get_next_user_state(user.id)
        bot.set_state(user.id, state)

        content_type, action, state_name = editor.state_parser(state)

        keyboard = editor.state_to_keyboard(state_name, state)
        msg = editor_msg[content_type][action][state_name][user.lang]

        bot.send_message(user.id, msg, reply_markup=keyboard)

    except StopIteration:
        state = bot.get_state(user.id)
        
        if state in editor.state_branches:
            states_iter = editor.state_branches[state][user_input].get_states_iter()
            editor.set_user_states(user.id, states_iter)
            user_state = editor.get_next_user_state(user.id)
            bot.set_state(user.id, user_state)

            state_category, state_group, state_name = editor.state_parser(user_state)

            msg = editor_msg[state_category][state_group][state_name][user.lang]
            keyboard = editor.state_to_keyboard(state_name)

            bot.send_message(user.id, msg, reply_markup=keyboard)

        else:
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

        editor.delete_user_responses(user.id)

        msg = editor_msg['confirmation']['confirm_response']['approved'][user.lang]
        bot.send_message(user.id, msg)

    elif call.data == 'cancel':
        editor.delete_user_responses(user.id)

        msg = editor_msg['confirmation']['confirm_response']['canceled'][user.lang]
        bot.send_message(user.id, msg)


@bot.callback_query_handler(func=lambda call: call.data != 'create_button')
def buttons_callback(call):
    view = call.data
    user = User(stg_users, call.from_user.id, call.from_user.language_code)
    vw.send(call.message.chat.id, view, user.lang)


bot.polling(none_stop=True)
