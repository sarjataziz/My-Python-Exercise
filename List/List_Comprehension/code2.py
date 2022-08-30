number  = [1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16,17,18,19,20]

even = [x for x in number if (x % 2 == 0)]
print(even)

odd = [y for y in number if (y % 2 != 0)]
print(odd)

print()

a = [num * 2 if num % 2 == 0 else num / 2 for num in number]
print(a)


print()
print("__________________________________")
print()

with_vowels = "This is so much fun!"

now = ''.join(char for char in with_vowels if char not in "aeiou")
print(now)