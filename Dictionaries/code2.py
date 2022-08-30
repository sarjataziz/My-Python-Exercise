numbers = dict(first = 1, secound = 2, third = 3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

print("____________________________________")

print({num : num ** 2 for num in [1,2,3,4,5,6,7,8,9,0]})

print("____________________________________")

str1 = "ABC"
str2 = "123"
combo = {str1[i] : str2[i] for i in range(0, len(str1))}
print(combo)

print("____________________________________")

num_list = [1,2,3,4,5,6,7,8,9,0]
print({n : ("even" if n % 2 == 0 else "odd") for n in num_list})

print("____________________________________")

