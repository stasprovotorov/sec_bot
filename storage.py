import os
import shelve
from functools import wraps


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

    @staticmethod
    def file_access(writeback=False) -> None:
        '''Decorator for opening and closing files in functions that work with them'''

        def decorator(func):
            @wraps(func)

            def wrapper(obj, *args, **kwargs):
                with shelve.open(obj.file_path, writeback=writeback) as db:
                    return func(obj, db, *args, **kwargs)
                 
            return wrapper
        
        return decorator


class StorageUsers(Storage):
    _FILENAME = 'data_users'
    _default_structure = {'users': dict, 'admins': set}

    @Storage._file_access()
    def get_user(self, db, id):
        return db['users'].get(id)

    @Storage._file_access(writeback=True)
    def save_user(self, db, id, lang, role):
        db['users'][id] = {'lang': lang, 'role': role}

    @Storage._file_access(writeback=True)
    def del_user(self, db, user_id):
        user_obj = db['users'].pop(user_id, None)
        if user_obj is None:
            raise KeyError(f'User with this ID {user_id} not found')

    @Storage._file_access()
    def get_admins(self, db):
        return db['admins']


class StorageContent(Storage):
    _FILENAME = 'data_content'
    _default_structure = {
        'view': dict,
        'text': dict,
        'image': dict,
        'button': dict
    }

    def lazy_init(self):
        self.view = StorageViews()
        self.text = StorageTexts()
        self.image = StorageImages()
        self.button = StorageButtons()


class StorageViews(StorageContent):
    PROTECTED_VIEWS = ['start']

    @Storage._file_access()
    def get(self, db, view_name):
        view_content_map = db['view'][view_name]
        view_data = {}

        for content_type, content_name in view_content_map.items():
            if content_type == 'button':
                view_data[content_type] = {
                    button_name: db[content_type].get(button_name) for button_name in content_name
                }
            else:
                view_data[content_type] = db[content_type].get(content_name)

        for content_type in db:
            if content_type != 'view' and content_type not in view_data:
                view_data.setdefault(content_type, None)

        return view_data

    @Storage._file_access()
    def get_all_view_names(self, db):
        return db['view'].keys()

    @Storage._file_access(writeback=True)
    def save(self, db, name, text, buttons, image=None):
        db['view'].setdefault(name, {})
        db['view'][name]['text'] = text
        db['view'][name]['button'] = buttons
        db['view'][name]['image'] = image

    @Storage._file_access(writeback=True)
    def delete(self, db, name):
        del db['view'][name]


class StorageTexts(StorageContent):
    PROTECTED_TEXTS = ('welcome')

    @Storage._file_access()
    def get(self, db, name, lang):
        return db['text'][name][lang]

    @Storage._file_access()
    def get_all_text_names(self, db):
        return db['text'].keys()

    @Storage._file_access(writeback=True)
    def save(self, db, name, text_ru=None, text_en=None):
        db['text'].setdefault(name, {})

        if text_ru and text_en:
            db['text'][name]['ru'] = text_ru
            db['text'][name]['en'] = text_en
        elif text_ru:
            db['text'][name]['ru'] = text_ru
        elif text_en:
            db['text'][name]['en'] = text_en

    @Storage._file_access(writeback=True)
    def delete(self, db, name):
        if name not in self.PROTECTED_TEXTS:
            del db['text'][name]


class StorageImages(StorageContent):
    @Storage._file_access()
    def get(self, db, name):
        return db['image'][name]
    
    @Storage._file_access()
    def get_all_image_names(self, db):
        return db['image'].keys()

    @Storage._file_access(writeback=True)
    def save(self, db, name, image):
        db['image'][name] = image

    @Storage._file_access(writeback=True)
    def delete(self, db, name):
        del db['image'][name]


class StorageButtons(StorageContent):
    PROTECTED_BUTTONS = ('editor', 'menu')

    @Storage._file_access()
    def get(self, db, name, lang):
        label = db['button'][name]['label'][lang]
        to_view = db['button'][name]['to_view']
        return label, to_view
    
    @Storage._file_access()
    def get_all_button_names(self, db):
        return list(db['button'].keys())

    @Storage._file_access(writeback=True)
    def save(self, db, name, label_ru, label_en, to_view):
        db['button'][name] = {
            'label': {'ru': label_ru, 'en': label_en},
            'to_view': to_view
        }

    @Storage._file_access(writeback=True)
    def save_label(self, db, button_name, label_lang, label):
        db['button'][button_name]['label'][label_lang] = label

    @Storage._file_access(writeback=True)
    def save_view(self, db, button_name, to_view):
        db['button'][button_name]['to_view'] = to_view

    @Storage._file_access(writeback=True)
    def delete(self, db, name):
        if name not in self.PROTECTED_BUTTONS:
            del db['button'][name]
