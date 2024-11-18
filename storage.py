from abc import ABC, abstractmethod
import shelve


class Storage(ABC):
    _FILENAME: str

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
        
    def get(self, key):
        with shelve.open(self._FILENAME) as db:
            return self._get(db, key)

    def save(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    @abstractmethod
    def _get(self):
        pass

    @abstractmethod
    def _save(self):
        pass

    @abstractmethod
    def _edit(self):
        pass

    @abstractmethod
    def _delete(self):
        pass


class StorageUsers(Storage):
    _FILENAME = 'data_users'
    _default_structure = {
        'users': dict, 
        'admins': list
    }

    def _get(self, db, key):
        return db[key]

    def _save(self):
        raise NotImplementedError

    def _edit(self):
        raise NotImplementedError

    def _delete(self):
        raise NotImplementedError
    

class StorageButtons(Storage):
    _FILENAME = 'data_buttons'
    _default_structure = {
        'buttons': dict
    }

    def _get(self, key):
        raise NotImplementedError

    def _save(self):
        raise NotImplementedError

    def _edit(self):
        raise NotImplementedError

    def _delete(self):
        raise NotImplementedError


class StorageContent(Storage):
    _FILENAME = 'data_content'
    _default_structure = {
        'text': dict,
        'images': dict
    }

    def _get(self, key):
        raise NotImplementedError

    def _save(self):
        raise NotImplementedError

    def _edit(self):
        raise NotImplementedError

    def _delete(self):
        raise NotImplementedError


if __name__ == '__main__':
    stg_users = StorageUsers()

    print(stg_users.get('users'))
