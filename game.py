# [] => this is an array
from random import randint
# arrays are indexed
# the index always starts at 0

choice = ["rock", "paper", "scissors"]

player_lives = 5
AI_lives = 5

total_lives = 5

player = False

while player is False:

	
	player = input("choose rock, paper or scissors:")

#player = True

#validate so that i can make a choice


# this will be the AI choice -> random pick from the choice
computer = choice[randint(0, 2)]
#print outputs whats in the round brackets


print("player chose:" + player)

# validate that the random choice worked for the AI
print("AI chose:" + computer)

if (computer == player):
	print("tie")

# check for negative conditions first

elif (computer == "rock"):
		if (player == "scissors"):
			print("You Lost! Try again!")
			player_lives -= 1
		else:
			print("You Won! Congratulations!")
			AI_lives -= 1

elif (computer == "paper"):
		if (player == "rock"):
			print("You Lost! Try again")
			player_lives -= 1
		else:
			print("You Won! Congratulations")
			AI_lives -= 1

elif (computer == "scissors"):
		if (player == "rock"):
			print("You Lost! Try again")
			player_lives -= 1
		else:
			print:("You Won! Congratulations")
			AI_lives -= 1

print("player_lives:", player_lives)
print("AI_lives:", AI_lives)

player = False