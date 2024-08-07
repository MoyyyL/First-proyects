# Data:
class Coins:
    def __init__(self, weight, wrapper):
        self.weight = weight
        self.wrapper = wrapper

penny = Coins(2.500, 50)
nickel = Coins(5.000, 40)
dime = Coins(2.268, 50)
quarter = Coins(5.670, 40)

coins = ["pennys", "nickels", "dimes", "quarters"]
weight = []

# get input
i = 0
while i < len(coins):
    try:
        how_many = int(input(f"Weight of your {coins[i]}: "))
        weight.append(how_many)
        i += 1
    except:
        print("i asked for a number")

