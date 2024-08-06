from moduleRPS import choosing, winner

#Get the input
player = input("Rock-Paper-Scissors: ")
player = player.lower()

# Computer choose
RPS = ["rock", "paper", "scissors"]
PC = choosing(RPS)

# loking for the winner

winner(player,PC)