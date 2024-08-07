# Data:
class Coins:
    def __init__(self, weight, wrapper, name):
        self.weight = weight
        self.wrapper = wrapper
        self.name = name

penny = Coins(2.500, 50, "penny")
nickel = Coins(5.000, 40, "nickel")
dime = Coins(2.268, 50, "dime")
quarter = Coins(5.670, 40, "quarter")

coins = [penny, nickel, dime, quarter]
weight = []
amount_of_wrappers = []


# get input
i = 0
while i < len(coins):
    try:
        how_many = int(input(f"Weight of your {coins[i].name}s: "))
        weight.append(how_many)
        i += 1
    except:
        print("i asked for a number")

# work the input

for i in range(len(weight)):
    coin_count = weight[i] / coins[i].weight
    print(coin_count)