import shelve


class Button:
    _filename = 'buttons_data'

    def __init__(self, label=None, func=None):
        self.id = self._set_id()
        self.label = label
        self.func = func

    @classmethod
    def _set_id(cls):
        with shelve.open(cls._filename) as db:
            count = db.get('count', 0) + 1
            db['count'] = count
            btn_id = f'BTN{count:02d}'
        return btn_id
