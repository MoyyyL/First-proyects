def new_values(abc):
    for i in range(len(abc)):
        abc[i] = abc[i]**2
    return abc

def check(abc):
    suma = sum(abc)
    for i in abc:
        if suma - i == i:
            return True
    return False