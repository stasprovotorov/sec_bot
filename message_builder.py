from telebot import TeleBot, types
from storage import StorageContent

class MessageBuilder:
    '''
    A class for assembling a message from content components in persistent storage for subsequent sending to the user. 
    The content components for the message are determined by the received key
    '''
    
    def __init__(self, bot: TeleBot, stg_content: StorageContent) -> None:
        self.bot = bot
        self.stg_content = stg_content


    def build_message(self, message_key: str, message_language: str) -> dict:
        '''Build a message from content components in persistent storage into a dictionary'''

        message_data = {}
        message_content = self.stg_content.views.get_view_content(message_key)
        
        for component_type, component_name in message_content.items():
            if component_type == 'text':
                message_data[component_type] = self.stg_content.texts.get_text(component_name, message_language)

            elif component_type == 'image':
                message_data[component_type] = self.stg_content.images.get_image(component_name)

            elif component_type == 'button':
                keyboard = types.InlineKeyboardMarkup()

                for button_name in component_name:
                    button_data = self.stg_content.buttons.get_button_data(button_name, message_language)
                    button_label, button_callback_data = button_data
                    keyboard.add(types.InlineKeyboardButton(button_label, callback_data=button_callback_data))
                    
                message_data[component_type] = keyboard

        return message_data
