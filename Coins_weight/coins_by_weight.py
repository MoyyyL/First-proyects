import math

# Data:
class Coins:
    def __init__(self, weight, wrapper, name, worth):
        self.weight = weight
        self.wrapper = wrapper
        self.name = name
        self.worth = worth

penny = Coins(2.500, 50, "pennies", 1)
nickel = Coins(5.000, 40, "nickels", 5)
dime = Coins(2.268, 50, "dimes", 10)
quarter = Coins(5.670, 40, "quarters", 25)

coins = [penny, nickel, dime, quarter]
weight = []
amount_of_wrappers = []
amount_of_coins = []


# get input
i = 0
while i < len(coins):
    try:
        how_many = int(input(f"Weight of your {coins[i].name}: "))
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
