from random import choice

def choosing(RPSC):
    pc = choice(RPSC)
    return pc

def winner(player,pc):
    if player == pc:
        return "Tie"
    elif pc == "scissors" and player == "paper":
        return "You lose"
    elif pc == "paper" and player == "rock":
        return "you lose"
    elif pc == "rock" and player == "scissors":
        return "you lose"
    else:
        return "You win"