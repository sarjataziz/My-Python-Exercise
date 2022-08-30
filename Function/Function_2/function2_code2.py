def sum_all_num(*args):
	total = 0
	for num in args:
		total += num 
	return total
nums = [1,2,3,4,5,6,7,8,9,0]
print(sum_all_num(*nums))


def display_name(first, second):
	print(f"{first} says hello to {second}")

names = {"first": "Sarjat", "second": "Luffy"}
display_name(**names)


def add_and_multiply_numbers(a,b,c):
	return a + b * c

data = dict(a = 1, b = 2, c = 3)

print(add_and_multiply_numbers(**data))
			