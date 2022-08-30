def eat_junk(food):
	assert food in [
		"pizza",
		"ice cream",
		"candy",
		], "Food must be junk food!"
	return f"I'm eating {food}"

food = input("Enter a food please: ")
print(eat_junk(food))