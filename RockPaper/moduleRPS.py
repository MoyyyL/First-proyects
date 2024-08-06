from random import choice

def asking(abc):
    while True:
        player = input("Rock-Paper-Scissors: ")
        player = player.lower()
        if player in abc:
            return player
        else:
            print("wrong")


def choosing(RPSC):
    pc = choice(RPSC)
    return pc


def winner(player,pc):
    if player == pc:
        return "Tie"
    elif pc == "scissors" and player == "paper":
        return False
    elif pc == "paper" and player == "rock":
        return False
    elif pc == "rock" and player == "scissors":
        return False
    else:
        return True