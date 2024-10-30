import shelve


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
        self._filename = 'users'

    def get_users(self):
        with shelve.open(self._filename) as db:
            return dict(db)
        
    def clear_users(self):
        with shelve.open(self._filename) as db:
            db.clear()

    def __getitem__(self, id):
        with shelve.open(self._filename) as db:
            if id in db:
                return db[id]
            else:
                raise KeyError(f'The user with this ID={id} is not found')

    def __setitem__(self, id, user_obj):
        if isinstance(user_obj, User):
            with shelve.open(self._filename) as db:
                db[id] = user_obj
        else:
            raise TypeError('Value must be an instance of User class')

    def __contains__(self, id):
        with shelve.open(self._filename) as db:
            return id in db
