import os
import shelve
from functools import wraps

from user import Language
from view import Image, Keyboard, Button, Text

class Storage():
    _FOLDER = 'data_storage'
    _FILENAME: str
    _default_structure: dict

    def __init__(self):
        for var in Storage.__annotations__:
            if not hasattr(self, var):
                raise AttributeError(f'Variable {var} is not defined in subclass {self.__class__.__name__}')
            if not getattr(self, var):
                raise ValueError(f'Variable {var} cannot be empty or None')
            
        if not os.path.exists(self._FOLDER):
            os.makedirs(self._FOLDER)
        
        self._file_path = os.path.join(self._FOLDER, self._FILENAME)
        self._init_file()

    def _init_file(self):
        with shelve.open(self._file_path, writeback=True) as db:
            for key, data_type in self._default_structure.items():
                db.setdefault(key, data_type())

    @staticmethod
    def _file_access(writeback=False):
        def decorator(func):
            @wraps(func)
            def wrapper(obj, *args, **kwargs):
                try:
                    with shelve.open(obj._file_path, writeback=writeback) as db:
                        return func(obj, db, *args, **kwargs)
                except FileNotFoundError as e:
                    raise RuntimeError(f'The file {obj._file_path} was not found') from e
                except PermissionError as e:
                    raise RuntimeError(f'You do not have permission to access the file {obj._file_path}') from e
                except OSError as e:
                    raise RuntimeError(f'An OS error occurred: {e}') from e
            return wrapper
        return decorator


class StorageUsers(Storage):
    _FILENAME = 'data_users'
    _default_structure = {'users': dict,  'admins': list, 'god': int}

    @Storage._file_access()
    def get_user(self, db, user_id):
        user_data = db['users'].get(user_id)
        if user_data is None:
            raise KeyError(f'User with this ID {user_id} not found')
        return user_data

    @Storage._file_access(writeback=True)
    def save_user(self, db, user_obj):
        db['users'][user_obj.user_id] = user_obj

    @Storage._file_access(writeback=True)
    def del_user(self, db, user_id):
        user_obj = db['users'].pop(user_id, None)
        if user_obj is None:
            raise KeyError(f'User with this ID {user_id} not found')

    @Storage._file_access()
    def is_admin(self, db, user_id):
        return user_id in db['admins']


class StorageContent(Storage):
    _FILENAME = 'data_content'
    _default_structure = {
        Text.__name__: dict, 
        Image.__name__: dict, 
        Keyboard.__name__: dict
    }

    @Storage._file_access()
    def get_content(self, db, content_type, content_key):
        return db[content_type.__name__][content_key]
    
    @Storage._file_access(writeback=True)
    def save_content(self, db, content_type, content_key, content_obj):
        db[content_type.__name__].update({content_key: content_obj})

    @Storage._file_access(writeback=True)
    def delete_content(self, db, content_type, content_key):
        del db[content_type.__name__][content_key]
