def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as e:
		print("Something went wrong!")
		print(e)
	else:
		print(f"{a} divided by {b} is {result}")

print(divide(1,9))
print(divide(1,0))