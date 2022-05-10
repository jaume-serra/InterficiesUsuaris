import sqlite3
DATABASE_NAME = "db.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def insert_tables():
    return

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS Plats(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL UNIQUE,
            descripcio TEXT,
            preu REAL NOT NULL,
            imatge BLOB,
            tipus TEXT NOT NULL
            )
            """
    ,
        """
          CREATE TABLE IF NOT EXISTS Comanda(
            numComanda INTEGER,
            plat TEXT,
            quantitat INTEGER NOT NULL,
            taula INTEGER,
            PRIMARY KEY (numComanda,plat)
            )
            """

        
        
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

create_tables()