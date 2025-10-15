import sqlite3

CONN = sqlite3.connect("taskmate.db")
CURSOR = CONN.cursor()
def initialize_db():
    """Create tables if they don't exist."""
    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)
    
    CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'Pending',
        project_id INTEGER,
        FOREIGN KEY (project_id) REFERENCES projects(id)
    )
    """)