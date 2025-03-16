'''
This module contains utility functions for building and sending messages
using the TeleBot library and the StorageContent class instance.
'''

from telebot import types
from storage import StorageContent

def build_message(stg_content: StorageContent, message_key: str, message_language: str) -> dict:
    '''Build a message from content components in persistent storage into a dictionary'''

    message_data = {}
    message_content = stg_content.views.get_view_content(message_key)
    
    for component_type, component_name in message_content.items():
        if component_type == 'text':
            message_data[component_type] = stg_content.texts.get_text(component_name, message_language)

        elif component_type == 'image':
            message_data[component_type] = stg_content.images.get_image(component_name)

        elif component_type == 'button':
            keyboard = types.InlineKeyboardMarkup()

            for button_name in component_name:
                button_data = stg_content.buttons.get_button_data(button_name, message_language)
                button_label, button_callback_data = button_data
                keyboard.add(types.InlineKeyboardButton(button_label, callback_data=button_callback_data))
                
            message_data[component_type] = keyboard

    return message_data
