from gameComponents import gameVars
def comparison(status):
		
	if (computer == gameVars.player):
		print("tie")

	# check for negative conditions first

	elif (computer == "scissors"):
			if (gameVars.player == "rock"):
				print("You Lost! Try again!")
				gameVars.player_lives -= 1
			else:
				print("You Won! Congratulations!")
				gameVars.AI_lives -= 1

	elif (computer == "rock"):
			if (gameVars.player == "paper"):
				print("You Lost! Try again")
				gameVars.player_lives -= 1
			else:
				print("You Won! Congratulations")
				gameVars.AI_lives -= 1

	elif (computer == "scissors"):
			if (gameVars.player == "paper"):
				print("You Lost! Try again")
				gameVars.player_lives -= 1
			else:
				print:("You Won! Congratulations")
				gameVars.AI_lives -= 1