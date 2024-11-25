class User:
    def __init__(self, id, lang):
        self._id = id
        self.lang = lang
        # self.role

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, _):
        raise AttributeError('User ID modification is not allowed')
    
    @id.deleter
    def id(self):
        raise AttributeError('User ID deletion is not allowed')
