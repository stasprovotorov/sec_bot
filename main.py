from dotenv import dotenv_values
from telebot.storage import StateMemoryStorage
from storage import StorageUsers, StorageContent
from user import User
from message_utils import build_message, send_message
from telebot import TeleBot

# Load the Telegram bot token from config.env
config = dotenv_values('config.env')
TELEGRAM_BOT_TOKEN = config['TELEGRAM_BOT_TOKEN']

# Initialize the Telegram bot object with a StateMemoryStorage object for storing user states
state_storage = StateMemoryStorage()
bot = TeleBot(TELEGRAM_BOT_TOKEN, state_storage=state_storage)

# Initialize the storage objects for the bot
stg_users = StorageUsers()
stg_content = StorageContent()


@bot.message_handler(commands=['start'])
def start(message):
    message_key = message.text.lstrip('/')
    user_id = message.from_user.id
    user_language = message.from_user.language_code
    user = User(stg_users, user_id, user_language)

    message_data = build_message(stg_content, user.user_id, message_key, user.user_language)
    send_message(bot, message_data)


bot.polling(none_stop=True)
