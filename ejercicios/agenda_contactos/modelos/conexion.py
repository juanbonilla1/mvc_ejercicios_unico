import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "data.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""CREATE TABLE IF NOT EXISTS agenda_contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT, telefono TEXT, direccion TEXT, correo TEXT
    );""")
    conn.commit()
    conn.close()
