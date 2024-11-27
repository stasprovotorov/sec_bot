from enum import Enum
from storage import StorageUsers

class Language(Enum):
    RU = 'LangRU'
    EN = 'LangEN'


class Roles(Enum):
    GOD = 'UserGod'
    ADMIN = 'UserAdmin'
    BASIC = 'UserBasic'


class User:
    def __init__(self, id, lang):
        self._id = id
        self.lang = lang
        self._init_role()

    def _init_role(self):
        self.role = Roles.ADMIN if StorageUsers.is_admin(self.id) else self.role = Roles.BASIC

    def switch_lang(self):
        self.lang = Language.RU if self.lang == Language.EN else Language.EN

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, _):
        raise AttributeError('User ID modification is not allowed')
    
    @id.deleter
    def id(self):
        raise AttributeError('User ID deletion is not allowed')
    
    @property
    def lang(self):
        return self._lang
    
    @lang.setter
    def lang(self, value):
        if value in ('ru', Language.RU):
            self._lang = Language.RU
        else:
            self._lang = Language.EN

    @lang.deleter
    def lang(self):
        raise AttributeError('User language deletion is not allowed')

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        if not isinstance(value, Roles):
            raise ValueError('Role must be an instance of class Roles')
        self._role = value
