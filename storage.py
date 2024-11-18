from abc import ABC, abstractmethod
import shelve


class Storage(ABC):
    _FILENAME: str

    def __init__(self):
        if not hasattr(self, '_FILENAME') or not self._FILENAME:
            raise ValueError('Filename is not set in subclass')

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class StorageUser(Storage):
    _FILENAME = 'data_users'

    def get(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError

    def edit(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


class StorageButton(Storage):
    _FILENAME = 'data_buttons'

    def get(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError

    def edit(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


class StorageContent(Storage):
    _FILENAME = 'data_content'

    def get(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError

    def edit(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
