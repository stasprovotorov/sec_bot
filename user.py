from storage import StorageUsers

class User:
    def __init__(self, id, lang):
        self._id = id
        self.lang = lang
        self._init_role()

    def switch_lang(self):
        self.lang = 'ru' if self.lang == 'en' else 'en'

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, _):
        raise AttributeError('User ID modification is not allowed')
    
    @id.deleter
    def id(self):
        raise AttributeError('User ID deletion is not allowed')
    
    @property
    def lang(self):
        return self._lang
    
    @lang.setter
    def lang(self, value):
        self._lang = value if value == 'ru' else 'en'

    @lang.deleter
    def lang(self):
        raise AttributeError('User language deletion is not allowed')

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        self._role = value
