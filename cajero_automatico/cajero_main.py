import sqlite3
import data_base
import functions

#* Menu 
general_menu = functions.menu()

#!data_base.open_create()


if (general_menu == 1): #crear cuenta
    functions.Crear_cuenta()
    
elif (general_menu == 2): # iniciar sesion
    
    if functions.password_verification():
        option = functions.account_menu()
        
        if option == 1:
            print(option)
                
        elif option == 2:
            print(option)
            
        elif option == 3:
            print(option)
        
        elif option == 4:
            print(option)
        
        elif option == 5:
            print(option)
        
        else:
            print("Alaberga que paso :VvVvVVvV")
    
    
elif (general_menu == 3): # salir
    pass



