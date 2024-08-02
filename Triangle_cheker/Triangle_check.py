from Modules import new_values, check

# getting input from the user
b = 0
sides = []

while b < 3:
    side = input(f"Give me the side {b +1}: ")
    
    try:
        side = float(side)
        sides.append(side)
        b += 1
    except ValueError:
        print("Please enter a number")

# Re-defining the values
new_sides = new_values(sides)

# Printing if is or not a Pythagorean triangle
if check(new_sides):
    print("Pythagorean Triangle")
else:
    print("This is not an Pythagorean triangle")