import sqlite3 as sql


def open_create():
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Accounts_database(
            Data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username text NOT NULL,
            Password text,
            NumberAcc integer UNIQUE,
            Balance text
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(Username, Password, N_acc, Balance):
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    
    try:
        instruccion = "INSERT INTO Accounts_database (Username, Password, NumberAcc, Balance) VALUES (?, ?, ?, ?)"
        cursor.execute(instruccion, (Username, Password, N_acc, Balance))
        
        conn.commit()
        return False
    
    except sql.IntegrityError:
        print("El numero de cuenta ya esta en uso, elige otro")
        return True
    
    finally:
        conn.close()

def UpdateFields(new_value, id_value):
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    
    # Usando placeholders (?) para evitar inyección SQL
    instruccion = "UPDATE Accounts_database SET Balance = ? WHERE Data_id = ?"
    cursor.execute(instruccion, (new_value, id_value))
    
    conn.commit()
    conn.close()

#! reparacion---------------------------------------
def deleteRow(id):
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    instruccion = "DELETE FROM Accounts_database WHERE Data_id = ?"
    cursor.execute(instruccion, (id,))
    
    conn.commit()
    conn.close()

def readRows(code):
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    
    
    instruccion = "SELECT NumberAcc FROM Accounts_database WHERE Data_id = ?"
    cursor.execute(instruccion, (code,))
    datos = cursor.fetchone()
    
    print(datos)
    conn.commit()
    conn.close()

def get_all_rows():
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    
    
    instruccion = "SELECT Data_id FROM Accounts_database"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    
    datos = [dato[0] for dato in datos]
    
    conn.commit()
    conn.close()
    return(datos)











def Search():
    conn = sql.connect("password_manager.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Password_database WHERE name='ibai'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    
    conn.commit()
    conn.close()
    print(datos)


