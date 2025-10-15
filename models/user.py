from db.connection import CONN, CURSOR

class User:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

        