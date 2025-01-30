from telebot import types

class View:
    def __init__(self, bot, stg_content):
        self.bot = bot
        self.stg_content = stg_content

    def send(self, chat_id, view_name, lang):
        view_data = self.stg_content.view.get(view_name)

        text = view_data['text'][lang]

        keyboard = types.InlineKeyboardMarkup()
        if view_data['button']:
            for button_data in view_data['button'].values():
                keyboard.add(
                    types.InlineKeyboardButton(
                        text=button_data['label'][lang], 
                        callback_data=button_data['to_view']
                    )
                )

        image = view_data['image']

        if image:
            self.bot.send_photo(chat_id, image, caption=text, reply_markup=keyboard)
        else:
            self.bot.send_message(chat_id, text, reply_markup=keyboard)
