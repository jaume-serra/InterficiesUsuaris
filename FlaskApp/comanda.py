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

def delete_commanda_plat(numComanda,plat):
    try:
        db = get_db()
        cursor = db.cursor()
        statement = "DELETE FROM Comanda WHERE numComanda = ? AND plat = ?"
        cursor.execute(statement, [numComanda,plat])
        db.commit()
        print("nerror")
        return True
    except:
        print("error")
        return False
def get_comanda_by_num(numComanda):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Comanda WHERE numComanda = ?"
    cursor.execute(statement, [numComanda])
    return cursor.fetchall()

def get_comanda_by_num_plat(numComanda,plat):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Comanda WHERE numComanda = ? AND plat = ?"
    cursor.execute(statement, [numComanda,plat])
    return cursor.fetchone()

def get_comanda_by_taula(taula):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Comanda WHERE taula = ?"
    cursor.execute(statement, [taula])
    return cursor.fetchall()


def get_comanda_all():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM Comanda"
    cursor.execute(statement)
    return cursor.fetchall()



# def get_comanda_from_date(data):
#     db = get_db()
#     cursor = db.cursor()
#     statement = "SELECT * FROM Comanda WHERE data >= ?"
#     cursor.execute(statement, [data])
#     return cursor.fetchall()