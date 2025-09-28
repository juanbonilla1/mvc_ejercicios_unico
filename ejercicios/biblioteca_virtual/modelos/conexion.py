import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "data.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""CREATE TABLE IF NOT EXISTS biblioteca_virtual (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT, autor TEXT, anio INTEGER, genero TEXT
    );""")
    conn.commit()
    conn.close()
