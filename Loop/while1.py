for x in range(1,11):
	print("*" * x)

print("-----------------------------------")

n = 1
while n <= 10:
	print("x" * n)
	n += 1

print("-----------------------------------")

for x in range(2):
	for num in range(1,11):
		print("a" * num)

print("-----------------------------------")

for num in range(1,11):
	count = 1
	a = ""
	while count <= num:
		a += "b"
		count += 1
	print(a)