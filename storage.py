import os
import shelve
from functools import wraps

from user import Language
from view import Image, Keyboard, Button

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
    _default_structure = {'text': dict, 'image': dict, 'keyboard': dict}


class StorageText(StorageContent):
    @Storage._file_access()
    def get_text(self, db, content_key, lang):
        text = db['text'].get(content_key)
        if text is None:
            raise KeyError(f'Text with content key {content_key} not found')
        return text[lang]

    @Storage._file_access(writeback=True)
    def add_text(self, db, content_key, text, lang):
        if db['text'].get(content_key):
            if db['text'][content_key].get(lang):
                KeyError(f'Text with content key {content_key} ang language {lang} already exists')
            db['text'][content_key].update({lang: text})
        else:
            db['text'][content_key] = {lang: text}

    @Storage._file_access(writeback=True)
    def edit_text(self, db, content_key, text, lang):
        db['text'][content_key][lang] = text

    @Storage._file_access(writeback=True)
    def delete_text(seld, db, content_key, lang=None):
        if lang is None:
            del db['text'][content_key]
        else:
            del db['text'][content_key][lang]


class StorageImage(StorageContent):
    @Storage._file_access()
    def get_image(self, db, content_key):
        return db['image'][content_key]
    
    @Storage._file_access(writeback=True)
    def save_image(self, db, content_key, image_obj):
        db['image'][content_key] = image_obj

    @Storage._file_access(writeback=True)
    def delete_image(self, db, content_key):
        del db['image'][content_key]


class StorageKeyboard(StorageContent):
    @Storage._file_access()
    def get_keyboard(self, db, content_key):
        return db['keyboard'][content_key]
    
    @Storage._file_access(writeback=True)
    def save_keyboard(self, db, content_key, keyboard):
        db['keyboard'][content_key] = keyboard

    @Storage._file_access(writeback=True)
    def delete_keyboard(self, db, content_key):
        del db['keyboard'][content_key]
