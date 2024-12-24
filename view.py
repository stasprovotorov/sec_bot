from user import Language
from io import BytesIO
from telebot import types

class Text:
    def __init__(self, content_ru, content_en):
        self.content = {
            Language.RU: content_ru,
            Language.EN: content_en
        }

    def __call__(self, language):
        return self.content[language]


class Image:
    def __init__(self, img_path):
        with open(img_path, 'rb') as img:
            self.img = img.read()

    def __call__(self):
        return BytesIO(self.img)


class Button:
    def __init__(self, label_ru, label_en, content_key_back):
        self.label = {Language.RU: label_ru, Language.EN: label_en}
        self.content_key_back = content_key_back
    
    def __call__(self, lang):
        return types.InlineKeyboardButton(self.label[lang], callback_data=self.content_key_back)


class Keyboard:
    def __init__(self):
        self.buttons = {}

    def add_button(self, button):
        self.buttons.update({button.label[Language.EN]: button})
    
    def delete_button(self, button):
        del self.buttons[button.label]
    
    def __call__(self, lang):
        keyboard = types.InlineKeyboardMarkup()
        for button in self.buttons.values():
            keyboard.add(button(lang))
        return keyboard


class View:
    def __init__(self, bot):
        self.bot = bot
        self.text = None
        self.image = None
        self.keyboard = None
    
    def set_text(self, content_key, stg_text, lang):
        obj_text = stg_text.get_text(content_key)
        self.text = obj_text.content[lang]

    def set_image(self, content_key, stg_image):
        obj_image = stg_image.get_image(content_key)
        self.image = obj_image()

    def set_keyboard(self, content_key, stg_keyboard, lang):
        obj_keyboard = stg_keyboard.get_keyboard(content_key)
        self.keyboard = obj_keyboard(lang)

    def send(self, chat_id, stg_content, key_content, language):
        text = stg_content.text.get_text(key_content)
        image = stg_content.image.get_image(key_content)
        keyboard = stg_content.keyboard.get_keyboard(key_content)
        if image:
            self.bot.send_photo(chat_id, photo=image(), caption=text(language), reply_markup=keyboard(language))
        else:
            self.bot.send_message(chat_id, text=text(language), reply_markup=keyboard(language))
