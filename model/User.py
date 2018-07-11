from util import passwordHandler


class User:

    def __init__(self, username, id):
        self.username = username
        self.id = id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @staticmethod
    def validate_login(password_hash, password):
        return passwordHandler.verify_password(password, password_hash)