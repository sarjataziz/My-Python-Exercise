def exponent(num, power = 2):       #power=2 default value
	return num ** power

print(exponent(2,3))
print(exponent(3,3))
print(exponent(4))
print(exponent(2))
print(exponent(6))


def add(a,b):
	return a + b
def math(a,b, fn = add):
	return fn(a,b)
def subtract(a,b):
	return a - b 

math(2,2)
math(2,2, subtract)