from db.connection import CONN, CURSOR

class Task:
    def __init__(self, title, project_id, status="Pending", id=None):
        self.id = id
        self.title = title
        self.status = status
        self.project_id = project_id

        