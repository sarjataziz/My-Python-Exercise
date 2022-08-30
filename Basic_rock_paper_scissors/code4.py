from random import randint

player = input("Player, make your move : ")

random_num = randint(0,2)

if random_num == 0 :
	Computer = "Rock"
elif random_num == 1 :
	Computer = "Paper"
else :
	Computer = "Scissors"
print("Computer plays : " ,Computer)

if player == Computer :
	print("It's tie!")
elif player == "Rock" :
	if Computer == "Scissors" :
		print("player wins...")
	else :
		print("Computer wins...")
elif player == "Paper" :
	if Computer == "Rock" :
		print("player wins...")
	else :
		print("Computer wins...")
elif player == "Scissors" :
	if Computer == "Rock" :
		print("Computer wins...")
	else :
		print("player wins...")
else :
	print("Try again....")