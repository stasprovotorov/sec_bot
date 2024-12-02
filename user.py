from enum import Enum

class Language(Enum):
    RU = 'LangRU'
    EN = 'LangEN'

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)


class Roles(Enum):
    GOD = 'UserGod'
    ADMIN = 'UserAdmin'
    BASIC = 'UserBasic'

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)


class User:
    def __init__(self, users_db, user_id, lang):
        try:
            user_obj = users_db.get_user(user_id)
            self.__dict__.update(user_obj.__dict__)
        except KeyError:
            self._user_id = user_id
            self.lang = lang
            self.role = Roles.ADMIN if users_db.is_admin(self.user_id) else Roles.BASIC
            users_db.save_user(self)

    def switch_lang(self):
        self.lang = Language.RU if self.lang == Language.EN else Language.EN

    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, _):
        raise AttributeError('User ID modification is not allowed')
    
    @user_id.deleter
    def user_id(self):
        raise AttributeError('User ID deletion is not allowed')
    
    @property
    def lang(self):
        return self._lang
    
    @lang.setter
    def lang(self, value):
        self._lang = Language.RU if value in ('ru', Language.RU) else Language.EN

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

    @role.deleter
    def role(self):
        raise AttributeError('User role deletion is not allowed')

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __repr__(self):
        attrs = ', '.join([f"{k}={v!r}" for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({attrs})'
