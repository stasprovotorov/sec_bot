from user import Language
from io import BytesIO
from telebot import types

class Text:
    def __init__(self, content_ru, content_en):
        self.lang = Language
        self.content = {
            self.lang.RU: content_ru,
            self.lang.EN: content_en
        }


class Image:
    def __init__(self, img_path):
        with open(img_path, 'rb') as img:
            self.img = img.read()


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
    def __init__(self, obj_bot, obj_user, obj_text=None, obj_image=None):
        self.bot = obj_bot
        self.user_id = obj_user.user_id
        self.text = obj_text.content[obj_user.lang] if obj_text else obj_text
        self.image = BytesIO(obj_image.img) if obj_image else obj_image
        
    def send(self):
        if self.text:
            self.bot.send_message(self.user_id, self.text)
        if self.image:
            self.bot.send_photo(self.user_id, self.image)
