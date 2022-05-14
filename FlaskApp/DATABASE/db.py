import sqlite3
DATABASE_NAME = "db.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def insert_tables():
    db = get_db()
    cursor = db.cursor()

    commanda_inserts = [
        "INSERT INTO Comanda VALUES (1, 'Macarrons', 2, 3, '2022-1-1 14:00:00')",
        "INSERT INTO Comanda VALUES (1, 'Filet', 2, 3, '2022-1-1 14:00:00')",
        "INSERT INTO Comanda VALUES (2, 'Hamburguesa', 3, 5, '2022-1-1 14:10:00')",
        "INSERT INTO Comanda VALUES (2, 'Nuggets', 4, 5, '2022-1-1 14:10:00')",
        "INSERT INTO Comanda VALUES (2, 'Coulant', 5, 5, '2022-1-1 14:10:00')"
    ]

    plats_inserts = [
        "INSERT INTO Plats VALUES (null, 'Amanida', 'Cesar', 5.5, null, 'Entrant')",
        "INSERT INTO Plats VALUES (null, 'Nuggets', 'De pollastre', 6, null, 'Entrant')",
        "INSERT INTO Plats VALUES (null, 'Macarrons', 'Salsa tomaquet', 7.5, null, 'Primer')",
        "INSERT INTO Plats VALUES (null, 'Hamburguesa', 'De formatge', 7, null, 'Primer')",
        "INSERT INTO Plats VALUES (null, 'Filet', null, 10.5, null, 'Segon')",
        "INSERT INTO Plats VALUES (null, 'Salmó', null, 9.5, null, 'Segon')",
        "INSERT INTO Plats VALUES (null, 'Coulant', 'Xocolata', 8.5, null, 'Postres')",
        "INSERT INTO Plats VALUES (null, 'Gelat', 'Vainilla', 5, null, 'Postres')"

    ]

    for c_insert in commanda_inserts:
        cursor.execute(c_insert)

    for p_insert in plats_inserts:
        cursor.execute(p_insert)
    
    db.commit()

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
            data DATETIME NOT NULL,
            PRIMARY KEY (numComanda,plat)
            )
            """

        
        
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

create_tables()
insert_tables()