import shelve
from functools import wraps

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

    @staticmethod
    def _file_access(writeback=False):
        def decorator(func):
            @wraps(func)
            def wrapper(obj, *args, **kwargs):
                try:
                    with shelve.open(obj._FILENAME, writeback=writeback) as db:
                        return func(obj, db, *args, **kwargs)
                except FileNotFoundError as e:
                    raise RuntimeError(f'The file {obj._FILENAME} was not found') from e
                except PermissionError as e:
                    raise RuntimeError(f'You do not have permission to access the file {obj._FILENAME}') from e
                except OSError as e:
                    raise RuntimeError(f'An OS error occurred: {e}') from e
            return wrapper
        return decorator


class StorageUsers(Storage):
    _FILENAME = 'data_users'
    _default_structure = {'users': dict,  'admins': list}

    @Storage._file_access()
    def get_user(self, db, user_id):
        user_obj = db['users'].get(user_id)
        if user_obj is None:
            raise KeyError(f'User with this ID {user_id} not found')
        return user_obj

    @Storage._file_access(writeback=True)
    def save_user(self, db, user_id, user_obj):
        db['users'][user_id] = user_obj

    @Storage._file_access(writeback=True)
    def del_user(self, db, user_id):
        user_obj = db['users'].pop(user_id, None)
        if user_obj is None:
            raise KeyError(f'User with this ID {user_id} not found')

    @classmethod
    @Storage._file_access()
    def get_admins(cls, db):
        print('!!!')


class StorageButtons(Storage):
    _FILENAME = 'data_buttons'
    _default_structure = {'buttons': dict}


class StorageContent(Storage):
    _FILENAME = 'data_content'
    _default_structure = {'text': dict, 'images': dict}


if __name__ == '__main__':
    StorageUsers.get_admins()
