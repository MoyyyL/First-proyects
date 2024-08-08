import math
from data import *


def check_zone():
    for i in range(len(coins)):
        how_many = input(f"Weight of your {coins[i].name}: ")