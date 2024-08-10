import math
from data import *


# revisando que el input sea correcto
def check_zone():
    i = 0 # como "for i" no se puede reiniciar como en C, usamos while mejor
    while i < len(coins):
        try:
            # si mete algo que no sea numero esto tira error y ejecuta el except:
            how_many = input(f"Weight of your {coins[i].name}: ")
            how_many = float(how_many)
            weight.append(how_many)
            i += 1
        except:
            print("i asked for a number")

# calculando la cantidad de monedas y de envoltorios para cada moneda
def Amount_of(pound_gram):
    
    if pound_gram == "lb":
        pound_gram = 454
    else:
        pound_gram = 1
    
    for i in range(len(weight)):
        # dividimos y dividimos mas lol
        coin_count = math.ceil((weight[i] * pound_gram) / coins[i].weight)
        wrappers = math.ceil(coin_count / coins[i].wrapper)
        
        amount_of_coins.append(coin_count)
        amount_of_wrappers.append(wrappers)

def calc_dollar():
    dollars = 0
    for i in range(len(amount_of_coins)):
        dollars += (coins[i].value * amount_of_coins[i])
    
    dollars = (dollars / 100)
    return dollars

def results_of(amount, object):
    for i in range(len(coins)):
        if i < len(coins) - 1:
            print(f"{amount[i]} {object[i].name},", end= " ")
        else:
            print(f"{amount[i]} {object[i].name}")