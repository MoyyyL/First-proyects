import sqlite3
import data_base
import functions

#* Menu 
general_menu = functions.menu()

#!data_base.open_create()


if (general_menu == 1): #crear cuenta
    functions.Crear_cuenta()
    
elif (general_menu == 2): # iniciar sesion
    
    Numero_de_cuenta = input("Ingresa tu numero de cuenta: ")
    
    if functions.password_verification(Numero_de_cuenta):
        option = functions.account_menu()
        
        if option == 1:
            functions.depositar(Numero_de_cuenta)
                
        elif option == 2:
            functions.retirar(Numero_de_cuenta)
            
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



