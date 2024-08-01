# get input from de user
b = 0

while b != 3:
    sides = input("give me the side of your triangle: ")
    
    if sides.isnumeric():
        print("hello world")
        b += 1
    else:
        print("Eso no es un numero")




