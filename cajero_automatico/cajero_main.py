import sqlite3
import data_base
import functions

#! solo de referencia
account_N = 0
users_name = ""
password = []

#* Menu 
general_menu = functions.menu()

#? Pruebas data_base



if (general_menu == 1): #crear cuenta
    functions.Crear_cuenta()
    
elif (general_menu == 2): # iniciar sesion
    print(2)
    
elif (general_menu == 3): # salir
    pass



