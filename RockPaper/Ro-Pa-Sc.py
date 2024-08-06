from moduleRPS import choosing, winner, asking

# Data
RPS = ["rock", "paper", "scissors"]
pc_points = 0
player_points = 0

# Getting all
while True:
    player = asking(RPS)
    PC = choosing(RPS)
    
    # loking for the winner
    win = winner(player,PC)
    print(f"Player: {player}" + "\n" f"PC: {PC}")
    
    # Printing winner
    if win == True:
        print("You win")
        player_points += 1
    elif win == False:
        print("You lose")
        pc_points += 1
    else:
        print(win)
    print(f"PC: {pc_points} / You: {player_points}")
    
    # again?
    ask = input("Want to play again?: ").lower()
    if ask in ["y", "yes", "yeah", "sure"]:
        pass
    else:
        break
