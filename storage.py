import shelve

class Storage():
    _FILENAME: str
    _default_structure: dict

    def __init__(self):
        for var in Storage.__annotations__:
            if not hasattr(self, var):
                raise AttributeError(f'Variable {var} is not defined in subclass {self.__class__.__name__}')
            if not getattr(self, var):
                raise ValueError(f'Variable {var} cannot be empty or None')
        
        self._init_file()

    def _init_file(self):
        with shelve.open(self._FILENAME, writeback=True) as db:
            for key, data_type in self._default_structure.items():
                db.setdefault(key, data_type())
                

class StorageUsers(Storage):
    _FILENAME = 'data_users'
    _default_structure = {'users': dict,  'admins': list}

    def get_user(self, user_id):
        with shelve.open(self._FILENAME) as db:
            user_obj = db['users'].get(user_id)
            if user_obj is None:
                raise KeyError(f'User with this ID {user_id} not found')
            return user_obj

    def save_user(self, user_id, user_obj):
        with shelve.open(self._FILENAME, writeback=True) as db:
            db['users'][user_id] = user_obj

    def del_user(self, user_id):
        with shelve.open(self._FILENAME, writeback=True) as db:
            user_obj = db['users'].pop(user_id, None)
            if user_obj is None:
                raise KeyError(f'User with this ID {user_id} not found')


class StorageButtons(Storage):
    _FILENAME = 'data_buttons'
    _default_structure = {'buttons': dict}


class StorageContent(Storage):
    _FILENAME = 'data_content'
    _default_structure = {'text': dict, 'images': dict}
