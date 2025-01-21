import os
import shelve
from functools import wraps

from user import Language, Roles
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
        'views': dict,
        'texts': dict,
        'images': dict,
        'buttons': dict
    }

    @Storage._file_access()
    def get_text(self, db, content_key, lang):
        text = db['text'].get(content_key)
        if text:
            return text[lang]
        return text

    @Storage._file_access(writeback=True)
    def save_text(self, db, content_key, lang, value):
        if db['text'].get(content_key):
            db['text'][content_key].update({lang: value})
        else:
            db['text'][content_key] = {lang: value}

    @Storage._file_access(writeback=True)
    def delete_text(self, db, content_key):
        del db['text'][content_key]

    @Storage._file_access()
    def get_image(self, db, content_key):
        return db['image'].get(content_key)    

    @Storage._file_access(writeback=True)
    def save_image(self, db, content_key, image_bytes):
        db['image'][content_key] = image_bytes

    @Storage._file_access(writeback=True)
    def delete_image(self, db, content_key):
        del db['image'][content_key]

    @Storage._file_access()
    def get_button(self, db, button_name, lang):
        label = db['button'][button_name]['label'][lang]
        content_key_back = db['button'][button_name]['content_key_back']
        return label, content_key_back

    @Storage._file_access(writeback=True)
    def save_button(self, db, button_name, lang, label, content_key_back):
        if db['button'].setdefault(button_name, {}):
            db['button'][button_name]['label'].update({lang: label})
        else:
            db['button'][button_name].update(
                {
                    'label': {lang: label},
                    'content_key_back': content_key_back
                }
            )

    @Storage._file_access(writeback=True)
    def delete_button(self, db, button_name):
        del db['button'][button_name]

    @Storage._file_access()
    def get_keyboard(self, db, content_key, lang, is_admin):
        keyboard = []
        for button_name in db['keyboard'][content_key]:
            keyboard.append(self.get_button(button_name, lang))
        if content_key == 'start' and is_admin:
            keyboard.append(self.get_button('Editor', lang))
        return keyboard

    @Storage._file_access(writeback=True)
    def save_keyboard(self, db, content_key, button_names):
        db['keyboard'][content_key] = button_names

    @Storage._file_access(writeback=True)
    def delete_keyboard(seld, db, content_key):
        del db['keyboard'][content_key]


if __name__ == '__main__':
    stg_content = StorageContent()
    
    with shelve.open(stg_content._file_path) as db:
        for key, value in dict(db).items():
            if key == 'images':
                continue
            print(key, value)
