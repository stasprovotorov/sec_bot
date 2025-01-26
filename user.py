class User:
    def __init__(self, stg_users, id, lang):
        if user_data := stg_users.get_user(id):
            self.id = id
            for attr, value in user_data.items():
                setattr(self, attr, value)
        else:
            self.id = id
            self.lang = lang
            self.role = self._determine_role(stg_users)
            stg_users.save_user(self.id, self.lang, self.role)

    def _determine_role(self, stg_users):
        return 'admin' if self.id in stg_users.get_admins() else 'basic'
    