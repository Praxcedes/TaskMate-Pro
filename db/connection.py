import sqlite3

CONN = sqlite3.connect("taskmate.db")
CURSOR = CONN.cursor()
