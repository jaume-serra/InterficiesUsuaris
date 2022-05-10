from DATABASE.db import get_db

def insert_comanda(numComanda, plat, quantitat, taula):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Comanda(numComanda, plat, quantitat, taula) VALUES (?, ?, ?, ?))"
    cursor.execute(statement, [numComanda, plat, quantitat, taula])
    db.commit()
    return True

def update_comanda(numActual, numComanda, plat, quantitat, taula):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Comanda SET numComanda = ?, plat = ?, quantitat = ?, taula = ? WHERE numComanda = ?"
    cursor.execute(statement, [numComanda, plat, quantitat, taula, numActual])
    db.commit()
    return True

def delete_commanda(numComanda):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Comanda WHERE numComanda = ?"
    cursor.execute(statement, [numComanda])
    db.commit()
    return True

def get_comanda_by_num(numComanda):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Comanda WHERE numComanda = ?"
    cursor.execute(statement, [numComanda])
    return cursor.fetchone()

def get_comanda_by_taula(taula):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Comanda WHERE taula = ?"
    cursor.execute(statement, [taula])
    return cursor.fetchall()