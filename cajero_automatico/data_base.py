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
    instruccion = "UPDATE Accounts_database SET Balance = ? WHERE NumberAcc = ?"
    cursor.execute(instruccion, (new_value, id_value))
    
    conn.commit()
    conn.close()

#UpdateFields(0, 12345678)
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

def get_balance(n_acc):
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    
    
    instruccion = "SELECT Balance FROM Accounts_database WHERE NumberAcc = ?"
    cursor.execute(instruccion, (n_acc,))
    datos = cursor.fetchone()
    
    conn.commit()
    conn.close()
    return(datos)


def get_password(n_acc):
    conn = sql.connect("accounts.db")
    cursor = conn.cursor()
    instruccion = f"SELECT Password FROM Accounts_database WHERE NumberAcc= ?"
    cursor.execute(instruccion, (n_acc,))
    datos = cursor.fetchone()
    
    conn.close()
    return(datos)


