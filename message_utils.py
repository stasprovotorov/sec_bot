'''
This module contains utility functions for building and sending messages
using the TeleBot library and the StorageContent class instance.
'''

from telebot import types, TeleBot
from storage import StorageContent


def build_message(stg_content: StorageContent, chat_id: int, message_key: str, message_language: str) -> dict:
    '''Build a message from content components in persistent storage into a dictionary.'''

    message_data = {'chat_id': chat_id}
    message_content = stg_content.message_content.get_view_content(message_key)
    
    for component_type, component_name in message_content.items():
        if component_type == 'text':
            text = stg_content.texts.get_text(component_name, message_language)
            parameter_name = 'caption' if 'image' in message_content else 'text'
            message_data[parameter_name] = text

        elif component_type == 'image':
            message_data['photo'] = stg_content.images.get_image(component_name)

        elif component_type == 'button':
            keyboard = types.InlineKeyboardMarkup()

            for button_name in component_name:
                button_data = stg_content.buttons.get_button_data(button_name, message_language)
                button_label, button_callback_data = button_data
                keyboard.add(types.InlineKeyboardButton(button_label, callback_data=button_callback_data))
                
            message_data['reply_markup'] = keyboard

    return message_data


def send_message(bot: TeleBot, message_data: dict) -> None:
    '''Send a message including photo and buttons using the specified message data.'''

    if 'photo' in message_data:
        bot.send_photo(**message_data)
    else:
        bot.send_message(**message_data)
