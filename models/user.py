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
     
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM users")
        rows = CURSOR.fetchall()
        return [cls(*row[1:], id=row[0]) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM users WHERE id=?", (id,))
        row = CURSOR.fetchone()
        return cls(*row[1:], id=row[0]) if row else None

