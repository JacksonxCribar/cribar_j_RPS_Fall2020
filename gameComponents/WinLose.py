
from gameComponents import gameVars
def winorlose(status):

	print("You ", status, " Try again some other time!")
	gameVars.choice = input("Y / N?")

	if gameVars.choice == "N" or gameVars.choice == "n":
		print("You chose to quit, have a good Day!")
		exit()

	elif gameVars.choice == "Y" or gameVars.choice == "y":
		gameVars.player_lives = 1
		gameVars.AI_lives = 1
		gameVars.player = False

	else:
		print("Please make a valid choice - Y or N")

	
				