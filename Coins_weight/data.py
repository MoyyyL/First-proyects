class Coins:
    def __init__(self, name, weight, wrapper, value):
        self.weight = weight
        self.wrapper = wrapper
        self.name = name
        self.value = value

penny = Coins("pennies", 2.500, 50, 1)
nickel = Coins("nickels", 5.000, 40, 5)
dime = Coins("dimes", 2.268, 50, 10)
quarter = Coins("quarters", 5.670, 40, 25)

coins = [penny, nickel, dime, quarter]
weight = []
amount_of_wrappers = []
amount_of_coins = []