from data import *
from modules_CW import check_zone, Amount_of, calc_dollar, results_of

# pounds or grams
while True:
        pound_gram = input("Pounds or grams lb/g: ")
        
        if pound_gram == "lb" or pound_gram == "g":
            break
        else:
            print("lb/g?")

# get input
check_zone()

# work the input
Amount_of(pound_gram) # calc of the coins and wrappers
dollar = calc_dollar() # how many dollars you have

# show the results
print("You have: ", end= "")
results_of(amount_of_coins, coins)

print("and you will need")
for i in range(len(amount_of_wrappers)):
    if i < len(amount_of_wrappers) - 1:
        print(f"{amount_of_wrappers[i]} wrappers for {coins[i].name},", end=" ")
    else:
        print(f"{amount_of_wrappers[i]} wrappers for {coins[i].name}")

print(f"and {dollar} dollars")
