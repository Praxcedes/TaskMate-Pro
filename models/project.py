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
  
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM projects")
        rows = CURSOR.fetchall()
        return [cls(*row[1:], id=row[0]) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM projects WHERE id=?", (id,))
        row = CURSOR.fetchone()
        return cls(*row[1:], id=row[0]) if row else None
    
    def delete(self):
        CURSOR.execute("DELETE FROM projects WHERE id=?", (self.id,))
        CONN.commit()