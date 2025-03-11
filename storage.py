import os
import shelve
from functools import wraps
from typing import Optional, KeysView
import exceptions


def file_access(writeback=False) -> None:
    '''Decorator for opening and closing files in methods that work with them'''

    def decorator(func):
        @wraps(func)
        def wrapper(obj, *args, **kwargs):
            with shelve.open(obj.file_path, writeback=writeback) as db:
                return func(obj, db, *args, **kwargs)            
        return wrapper
    
    return decorator


class StorageBase:
    '''A base class for working with data from persistent storage'''

    file_name: str
    default_file_structure: dict

    folder_name = 'data_storage'

    def __init__(self) -> None:
        # Checking required variables in the subclass
        for annotation in StorageBase.__annotations__:
            if not hasattr(self, annotation):
                raise AttributeError(
                    f'Variable <{annotation}> is not defined in subclass <{self.__class__.__name__}>'
                )
            
            if getattr(self, annotation) is None:
                raise ValueError(f'Variable <{annotation}> cannot be empty or None')
        
        # Creating storage folder it if it does not exist
        os.makedirs(StorageBase.folder_name, exist_ok=True)
        
        self.file_path = os.path.join(StorageBase.folder_name, self.file_name)
        
        # Checking the storage file and creating it if it does not exist
        if not os.path.exists(self.file_path):
            with shelve.open(self.file_path, writeback=True) as db:
                for key, value in self.default_file_structure.items():
                    db.setdefault(key, value)


class StorageUsers(StorageBase):
    '''A class for working with users data from persistent storage'''

    file_name = 'data_users'
    default_file_structure = {'users': {}, 'admins': set()}

    @file_access()
    def get_user(self, db, user_id: int) -> Optional[dict]:
        return db['users'].get(user_id)

    @file_access(writeback=True)
    def save_user(self, db, user_id: int, user_language: str, user_role: str) -> None:
        if db['users'].get(user_id):
            raise exceptions.UserAlreadyExistsError(user_id)
        
        db['users'][user_id] = {'user_language': user_language, 'user_role': user_role}

    @file_access(writeback=True)
    def delete_user(self, db, user_id: int) -> None:
        if user_id not in db['users']:
            raise exceptions.UserNotFoundError(user_id)
        
        db['users'].pop(user_id)

    @file_access()
    def is_user_admin(self, db, user_id: int) -> bool:
        return user_id in db['admins']


class StorageContent(StorageBase):
    '''Composite class for bot content component classes'''

    file_name = 'data_content'
    default_file_structure = {'view': {}, 'text': {}, 'image': {}, 'button': {}}

    def __init__(self) -> None:
        super().__init__()
        self.views = StorageViews(self.file_path)
        self.texts = StorageTexts()
        self.images = StorageImages()
        self.buttons = StorageButtons()


class StorageViews():
    '''Component class for working with bot content component views in persistent storage'''

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    @file_access()
    def get_view_content(self, db, view_name: str) -> Optional[dict]:
        '''Get a dictionary with the names of content components by view name'''

        if view := db['view'].get(view_name):
            return view
        
        raise exceptions.ViewNotFoundError(view_name)

    @file_access()
    def get_view_names(self, db) -> Optional[KeysView]:
        '''Get all view names in persistent storage or None'''

        if view_names := db['view'].keys():
            return view_names

    @file_access(writeback=True)
    def create_view(
        self, 
        db, 
        view_name: str, 
        text_name: str, 
        button_names: Optional[list[str]] = None, 
        image_name: Optional[str] = None
    ) -> None:
        '''Save view in persistent storage'''

        new_view = db['view'].setdefault(view_name, {})
        if new_view:
            raise exceptions.ViewAlreadyExistsError(view_name)
        
        new_view['text'] = text_name
        if button_names:
            new_view['button'] = button_names
        if image_name:
            new_view['image'] = image_name

    @file_access(writeback=True)
    def delete_view(self, db, view_name: str) -> None:
        '''Delete view from persistent storage'''

        try:
            db['view'].pop(view_name)
        except KeyError:
            raise exceptions.ViewNotFoundError(view_name)


class StorageTexts():
    '''Component class for working with text components of bot content in persistent storage'''

    @file_access()
    def get(self, db, name, lang):
        return db['text'][name][lang]

    @file_access()
    def get_all_text_names(self, db):
        return db['text'].keys()

    @file_access(writeback=True)
    def save(self, db, name, text_ru=None, text_en=None):
        db['text'].setdefault(name, {})

        if text_ru and text_en:
            db['text'][name]['ru'] = text_ru
            db['text'][name]['en'] = text_en
        elif text_ru:
            db['text'][name]['ru'] = text_ru
        elif text_en:
            db['text'][name]['en'] = text_en

    @file_access(writeback=True)
    def delete(self, db, name):
        if name not in self.PROTECTED_TEXTS:
            del db['text'][name]


class StorageImages():
    @file_access()
    def get(self, db, name):
        return db['image'][name]
    
    @file_access()
    def get_all_image_names(self, db):
        return db['image'].keys()

    @file_access(writeback=True)
    def save(self, db, name, image):
        db['image'][name] = image

    @file_access(writeback=True)
    def delete(self, db, name):
        del db['image'][name]


class StorageButtons():
    PROTECTED_BUTTONS = ('editor', 'menu')

    @file_access()
    def get(self, db, name, lang):
        label = db['button'][name]['label'][lang]
        to_view = db['button'][name]['to_view']
        return label, to_view
    
    @file_access()
    def get_all_button_names(self, db):
        return list(db['button'].keys())

    @file_access(writeback=True)
    def save(self, db, name, label_ru, label_en, to_view):
        db['button'][name] = {
            'label': {'ru': label_ru, 'en': label_en},
            'to_view': to_view
        }

    @file_access(writeback=True)
    def save_label(self, db, button_name, label_lang, label):
        db['button'][button_name]['label'][label_lang] = label

    @file_access(writeback=True)
    def save_view(self, db, button_name, to_view):
        db['button'][button_name]['to_view'] = to_view

    @file_access(writeback=True)
    def delete(self, db, name):
        if name not in self.PROTECTED_BUTTONS:
            del db['button'][name]
