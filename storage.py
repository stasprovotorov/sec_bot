import shelve


class Storage():
    _FILENAME: str
    _default_structure: dict

    def __init__(self):
        if not hasattr(self, '_FILENAME') or not self._FILENAME:
            raise AttributeError(f'Filename is not set in subclass {self.__class__.__name__}')
        
        if not hasattr(self, '_default_structure') or not self._default_structure:
            raise AttributeError(f'Default file structure is not set in subclass {self.__class__.__name__}')
        
        self._init_file()

    def _init_file(self):
        with shelve.open(self._FILENAME, writeback=True) as db:
            for key, data_type in self._default_structure.items():
                db.setdefault(key, data_type())


class StorageUsers(Storage):
    _FILENAME = 'data_users'
    _default_structure = {
        'users': dict, 
        'admins': list
    }


class StorageButtons(Storage):
    _FILENAME = 'data_buttons'
    _default_structure = {
        'buttons': dict
    }


class StorageContent(Storage):
    _FILENAME = 'data_content'
    _default_structure = {
        'text': dict,
        'images': dict
    }
