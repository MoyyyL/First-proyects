# importing an built-in module 
from random import randrange
import time

# Response list
Responses = {
    1 : "Yes",
    2 : "No",
    3 : "Maybe",
    4 : "Hell no",
    5 : "Hell yeah",
    6 : "ask yourself",
    7 : "i don't think so",
    8 : "That's right",
    9 : "Did you just read my mind?",
    10 : "gross",
    11 : "why not?",
    12 : "yepe",
    13 : "Trow a coin",
    14 : "What kind of question is that?",
    15 : "eh....",
    16 : "again",
    17 : "am I even real?",
    18 : "easter egg",
    19 : "Bro what?",
    20 : "definitely"
}

# Choosing
def Choosing():
    num = randrange(1, 21)
    choosen_word = Responses.get(num)
    return choosen_word

# asking
def ask_input():
    # Getting the question of the user
    input("ask something to the magic 8 ball: ")
    print("Thinking....")
    time.sleep(2)
    
    response = Choosing()
    print(response)

# Loop 
while True:
    ask_input()
    
    again = input("Wanna ask something else? Yes/No: ")
    L_again = again.lower()
    
    if L_again in ["yes", "y", "yeah", "why not?", "for sure"]:
        continue
    elif L_again in ["no", "n", "hell no"]:
        break
    else:
        print("I'll take it as a yes")
