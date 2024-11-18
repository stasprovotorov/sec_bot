from abc import ABC, abstractmethod
import shelve


class Storage(ABC):
    _FILENAME: str

    def __init__(self):
        if not hasattr(self, '_FILENAME') or not self._FILENAME:
            raise ValueError('Filename is not set in subclass')
        
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


class StorageUser(Storage):
    _FILENAME = 'data_users'

    def _get(self, db, key):
        return key

    def _save(self):
        raise NotImplementedError

    def _edit(self):
        raise NotImplementedError

    def _delete(self):
        raise NotImplementedError
    
    def get_admins(self):
        pass

    def add_admin(self):
        pass


class StorageButton(Storage):
    _FILENAME = 'data_buttons'

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

    def _get(self, key):
        raise NotImplementedError

    def _save(self):
        raise NotImplementedError

    def _edit(self):
        raise NotImplementedError

    def _delete(self):
        raise NotImplementedError


if __name__ == '__main__':
    stg_user = StorageUser()

    stg_user.get(171025409)
