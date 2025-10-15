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