import data_base
import random

def menu():
    print("--------------select an option-----------------")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")
    print("-----------------------------------------------")
    
    while(True):
        try:
            option = int(input())
            if option < 1 or option > 3:
                print("Select an option from the menu")
            else:
                return option
        except ValueError:
            print("Use just numbers beetween in the 1-3 range")

#? Opcion 1

def Crear_cuenta():
    
    while(True):
        try:
            username = input("ingrese el nombre de la cuenta: ")
            if username.isdigit():
                raise ValueError
        
            password = input("ingrese la contraseña: ")
            balance = 0
            
            while (True):
                try:
                    n_acc = input("Ingrese un numero de cuenta unico de 8 digitos: ")
                    
                    if len(n_acc) == 8 and n_acc.isdigit():
                        int(n_acc)
        
                        if data_base.insertRow(username, password, n_acc, balance):
                            # se vuelve a intentar el numero de cuenta diferente
                            pass
                        else:
                            #Se creo exitosamente
                            return #* retorna asi saliendo de la funcion completamente
                    else:
                        raise ValueError
                
                except ValueError:
                    print("El numero debe ser de 8 DIGITOS")
        
        except ValueError:
            print("Ingrese un valor apropiado")



#?-------------------


def account_menu():
    print("-----------------Account menu-----------------------")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Ver historial de transaccion")
    print("5. Cerrar sesion")
    
    while(True):
        try:
            option = int(input())
            if option < 1 or option > 5:
                print("Select an option from the menu")
            else:
                return option
        except ValueError:
            print("Use just numbers beetween in the 1-3 range")