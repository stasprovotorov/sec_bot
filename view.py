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
    def __init__(self, bot, stg_content):
        self.bot = bot
        self.stg_content = stg_content
        self.text = None
        self.image = None
        self.keyboard = None

    def get_text(self, content_key, language):
        self.text = self.stg_content.text.get_text(content_key)[language] # ![language] -> _get_content
        return self.text
    
    def get_image(self, content_key):
        self.image = self.stg_content.image.get_image(content_key)
        return self.image
