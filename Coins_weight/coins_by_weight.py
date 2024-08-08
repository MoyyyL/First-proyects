import math
from data import *
import modules_CW

# get input
i = 0
while i < len(coins):
    try:
        how_many = int()
        weight.append(how_many)
        i += 1
    except:
        print("i asked for a number")

# work the input

for i in range(len(weight)):
    coin_count = round(weight[i] / coins[i].weight)
    wrappers = math.ceil(coin_count / coins[i].wrapper)
    
    amount_of_coins.append(coin_count)
    amount_of_wrappers.append(wrappers)

# show the things
