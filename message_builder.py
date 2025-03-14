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
