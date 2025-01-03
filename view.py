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

    def _get_text(self, content_key, lang):
        return self.stg_content.get_text(content_key, lang)

    def _get_image(self, content_key):
        return self.stg_content.get_image(content_key)

    def _get_keyboard(self, content_key, lang):
        buttons_data = self.stg_content.get_keyboard(content_key, lang)
        keyboard = types.InlineKeyboardMarkup()
        for label, content_key_back in buttons_data:
            keyboard.add(types.InlineKeyboardButton(label, callback_data=content_key_back))
        return keyboard

    def send(self, chat_id, content_key, lang):
        text = self._get_text(content_key, lang)
        image = self._get_image(content_key)
        keyboard = self._get_keyboard(content_key, lang)
        if image:
            self.bot.send_photo(chat_id, image, caption=text, reply_markup=keyboard)
        else:
            self.bot.send_message(chat_id, text, reply_markup=keyboard)
