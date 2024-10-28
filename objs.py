class User:
    def __init__(self, language):
        self.language = language

    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self, value):
        self._language = value


class Users:
    def __init__(self):
        self.users = {}

    def __getitem__(self, id):
        if id in self.users:
            return self.users[id]
        raise KeyError(f'The user with this ID is not found')

    def __setitem__(self, id, user_obj):
        if isinstance(user_obj, User):
            self.users[id] = user_obj
        else:
            raise TypeError('Value must be an instance of User class')
