player1 = input("Player 1, make your move : ")
player2 = input("Player 2, make your move : ")

if player1 == player2 :
	print("It's tie!")
elif player1 == "Rock" :
	if player2 == "Scissors" :
		print("player1 wins...")
	elif player2 == "Paper" :
		print("player2 wins...")
elif player1 == "Paper" :
	if player2 == "Rock" :
		print("player1 wins...")
	elif player2 == "Scissors" :
		print("player2 wins...")
elif player1 == "Scissors" :
	if player2 == "Rock" :
		print("player2 wins...")
	elif player2 == "Paper" :
		print("player1 wins...")
else :
	print("Try again....")