# get input from de user
b = 0
sides = []

while b < 3:
    side = input(f"Give me the side {b +1}: ")
    
    try:
        side = float(side)
        sides.append(side)
        b += 1
        print("aña")
    except ValueError:
        print("Please enter a number")

