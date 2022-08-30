def fibonacci_func(max):
	nums = []
	a, b = 0, 1
	while len(nums) < max:
		nums.append(b)
		a, b = b, a + b 
	return nums

print(fibonacci_func(10))

print("**********************************")

def fibonacci_gen(max):
	x = 0
	y = 1
	count = 0
	while count < max:
		x, y = y, x+y 
		yield x 
		count += 1
print(fibonacci_gen(10))

for n in fibonacci_gen(10):
	print(n)