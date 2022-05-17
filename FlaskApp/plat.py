
from DATABASE.db import get_db

def insert_plat(nom, descripcio, preu, imatge, tipus):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Plats(nom, descripcio, preu, imatge, tipus) VALUES (?, ?, ?, ?, ?))"
    cursor.execute(statement, [nom, descripcio, preu, imatge, tipus])
    db.commit()
    return True

def update_plat(nomActual, nom, descripcio, preu, imatge, tipus):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Plats SET nom = ?, decripcio = ?, preu = ?, imatge = ?, tipus = ? WHERE nom = ?"
    cursor.execute(statement, [nom, descripcio, preu, imatge, tipus, nomActual])
    db.commit()
    return True

def delete_plat(nomPlat):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Plats WHERE nom = ?"
    cursor.execute(statement, [nomPlat])
    db.commit()
    return True

def get_plat_by_nom(nomPlat):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Plats WHERE nom = ?"
    cursor.execute(statement, [nomPlat])
    return cursor.fetchone()

def get_plat_by_tipus(tipusPlat):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Plats WHERE tipus = ?"
    cursor.execute(statement, [tipusPlat])
    return cursor.fetchall()

def get_carta():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Plats"
    cursor.execute(statement)
    return cursor.fetchall()