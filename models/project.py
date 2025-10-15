from db.connection import CONN, CURSOR

class Project:
    def __init__(self, name, user_id, id=None):
        self.id = id
        self.name = name
        self.user_id = user_id

    @classmethod
    def create(cls, name, user_id):
        CURSOR.execute("INSERT INTO projects (name, user_id) VALUES (?, ?)", (name, user_id))
        CONN.commit()
        return cls(name, user_id, CURSOR.lastrowid)
  