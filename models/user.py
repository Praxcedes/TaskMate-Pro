from db.connection import CONN, CURSOR

class User:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def create(cls, name, email):
        CURSOR.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        CONN.commit()
        return cls(name, email, CURSOR.lastrowid)    

