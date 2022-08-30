nested_list = [[1,2,3], [4,5,6], [7,8,9]]

print(nested_list[1][1])
print(nested_list[2][2])

for x in nested_list:
	for val in x:
		print(val)    # print: 1, 2, 3, 4, 5, 6, 7, 8, 9

for x in nested_list:
	print(x)          # print: [1, 2, 3] [4, 5, 6] [7, 8, 9]


[[print(v) for v in p] for p in nested_list]   # print: 1, 2, 3, 4, 5, 6, 7, 8, 9