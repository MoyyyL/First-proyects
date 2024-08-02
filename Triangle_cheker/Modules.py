# Updating the values to their square to make the math more easy
def new_values(abc):
    for i in range(len(abc)):
        abc[i] = abc[i]**2
    return abc

# checking if the sum of 2 is iqual to the third left
def check(abc):
    suma = sum(abc)
    for i in abc:
        if suma - i == i:
            return True
    return False