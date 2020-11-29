# [] => this is an array
from random import randint
from gameComponents import gameVars, WinLose, comparison
# arrays are indexed
# the index always starts at 0

#choice = ["rock", "paper", "scissors"]

#player_lives = 1
#AI_lives = 1

#total_lives = 1



#player = False

while gameVars.player is False:
	print("=====*RPS GAME*=====")
	print("computer_lives:", gameVars.AI_lives, "/", gameVars.total_lives)
	print("player_lives:", gameVars.AI_lives, "/", gameVars.total_lives)
	print("====================")

	print("Choose your weapons of choice! Rock, Paper, Or Scissors, or if you don't feel like playing type quit\n")
	
	

	gameVars.player = input("Welcome to the Game! Choose Rock, Paper, Or Scissors: \n")

	if gameVars.player == "quit":
		print("You Chose to quit! Truly Unfortunate")
		exit()

#player = True

#validate so that i can make a choice


#this will be the AI choice -> random pick from the choice
	computer = gameVars.choice[randint(0, 2)]
#print outputs whats in the round brackets


	print("You chose:" + gameVars.player)

	# validate that the random choice worked for the AI
	print("AI chose:" + computer)

	# if (computer == gameVars.player):
	# 	print("tie")

	# # check for negative conditions first

	# elif (computer == "scissors"):
	# 		if (gameVars.player == "rock"):
	# 			print("You Lost! Try again!")
	# 			gameVars.player_lives -= 1
	# 		else:
	# 			print("You Won! Congratulations!")
	# 			gameVars.AI_lives -= 1

	# elif (computer == "rock"):
	# 		if (gameVars.player == "paper"):
	# 			print("You Lost! Try again")
	# 			gameVars.player_lives -= 1
	# 		else:
	# 			print("You Won! Congratulations")
	# 			gameVars.AI_lives -= 1

	# elif (computer == "scissors"):
	# 		if (gameVars.player == "paper"):
	# 			print("You Lost! Try again")
	# 			gameVars.player_lives -= 1
	# 		else:
	# 			print:("You Won! Congratulations")
	# 			gameVars.AI_lives -= 1

	if gameVars.player_lives == 0:
		WinLose.winorlose("Lose")
			# 	print("You Lost! Try agian some other time!")
			# 	gameVars.choice = input("Y / N?")

			# 	if gameVars.choice == "N" or gameVars.choice == "n":
			# 		print("You chose to quit, have a good Day!")
			# 		exit()

			# elif gameVars.choice == "Y" or gameVars.choice == "y":
			# 	gameVars.player_lives = 1
			# 	gameVars.AI_lives = 1
			# 	gameVars.player = False

			# else:
				# print("Please make a valid choice - Y or N")


	if gameVars.AI_lives == 0:
		WinLose.winorlose("Won")
			# print("You Won! Try againn some other time!")
			# choice = input("Y / N?")

			# if gameVars.choice == "N" or gameVars.choice == "n":
			# 	print("You chose to quit, have a good Day!")
			# 	exit()

			# elif gameVars.choice == "Y" or gameVars.choice == "y":
			# 	gameVars.player_lives = 1
			# 	gameVars.AI_lives = 1
			# 	gameVars.player = False

			# else:
			# 	print("Please make a valid choice - Y or N")



	print("player_lives:", gameVars.player_lives)
	print("AI_lives:", gameVars.AI_lives)

	gameVars.player = False