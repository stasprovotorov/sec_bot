from telebot import types

class View:
    def __init__(self, bot, stg_content):
        self.bot = bot
        self.stg_content = stg_content

    # def send(self, chat_id, view, lang, role=None):
    #     view_data = self.stg_content.views.get(view)
        
    #     text = self.stg_content.texts.get(view_data['text'], lang)

    #     keyboard = types.InlineKeyboardMarkup()
    #     buttons_data = []
        

    #     if view_data['buttons']:
            
    #         for button_name in view_data['buttons']:
    #             buttons_data.append(self.stg_content.buttons.get(button_name, lang))

    #         if view == 'start' and role == 'admin':
    #             buttons_data.append(self.stg_content.buttons.get('Editor', lang))

    #         for label, view_next in buttons_data:
    #             keyboard.add(types.InlineKeyboardButton(label, callback_data=view_next))

    #     if image := view_data['image']:
    #         image = self.stg_content.images.get(image)
    #         self.bot.send_photo(chat_id, image, caption=text, reply_markup=keyboard)
    #     else:
    #         self.bot.send_message(chat_id, text, reply_markup=keyboard)


    def send(self, chat_id, view_name, lang, role=None):
        view_data = self.stg_content.view.get(view_name)
        print(view_data)

