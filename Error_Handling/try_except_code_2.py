while True:
	try:
		num = int(input("Please enter a number : "))
	except:
		print("That's not a number!")
	else:
		print("Great job! You did it..")
		break
	finally:
		print("Runs every times")