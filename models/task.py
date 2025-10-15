from db.connection import CONN, CURSOR

class Task:
    def __init__(self, title, project_id, status="Pending", id=None):
        self.id = id
        self.title = title
        self.status = status
        self.project_id = project_id

    @classmethod
    def create(cls, title, project_id):
        CURSOR.execute("INSERT INTO tasks (title, project_id) VALUES (?, ?)", (title, project_id))
        CONN.commit()
        return cls(title, project_id, id=CURSOR.lastrowid)
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM tasks")
        rows = CURSOR.fetchall()
        return [cls(*row[1:], id=row[0]) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM tasks WHERE id=?", (id,))
        row = CURSOR.fetchone()
        return cls(*row[1:], id=row[0]) if row else None