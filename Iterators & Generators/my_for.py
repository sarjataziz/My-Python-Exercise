def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			things = next(iterator)
		except StopIteration:
			break
		else:
			func(things)

def square(x):
	print(x * x)

my_for("Hello", print)
print()
my_for([1,2,3,4,5,6,7,8,9,0], square)