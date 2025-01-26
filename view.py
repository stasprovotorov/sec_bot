from telebot import types

class View:
    def __init__(self, bot, stg_content):
        self.bot = bot
        self.stg_content = stg_content

    def send(self, chat_id, view, lang, role):
        view_data = self.stg_content.views.get(view)
        
        text = self.stg_content.texts.get(view_data['text'], lang)

        buttons_data = []
        for button_name in view_data['buttons']:
            buttons_data.append(self.stg_content.buttons.get(button_name, lang))

        if role == 'admin':
            buttons_data.append(self.stg_content.buttons.get('Editor', lang))

        keyboard = types.InlineKeyboardMarkup()
        for label, view_next in buttons_data:
            keyboard.add(types.InlineKeyboardButton(label, callback_data=view_next))

        if image := view_data['image']:
            image = self.stg_content.images.get(image)
            self.bot.send_photo(chat_id, image, caption=text, reply_markup=keyboard)
        else:
            self.bot.send_message(chat_id, text, reply_markup=keyboard)
