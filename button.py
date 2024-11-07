import shelve


class Button:
    def __init__(self, label_ru, label_en, func):
        self.id = self.set_id()
        self.label = {'ru': label_ru, 'en': label_en}
        self.func = func

    _filename = 'buttons_data'

    @classmethod
    def set_id(cls):
        with shelve.open(cls._filename) as db:
            counter = db.get('counter', 0) + 1
            db['counter'] = counter
        return f'BTN{counter:02d}'
