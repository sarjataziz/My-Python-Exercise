num = [1,2,3,4,5,6,7,8,9,0]

d_n = [x * 10 for x in num]
print(d_n)

print()
print("_________________________________________")
print()

number = [1,2,3,4,5,6,7,8,9,0]
double_numbers = []

for x in number:
	double_number = x * 10
	double_numbers.append(double_number)
print(double_number)


print()
print()
print("_________________________________________")
print()

friends = ['ashley', 'matt', 'michael']
     
[friend[0].upper() for friend in friends] # ['Ashley', 'Matt', 'Michael']


print()
print("_________________________________________")
print()


friends = ['ashley', 'matt', 'michael']
     
[friend[0].upper() + friend[1:] for friend in friends] # this actually returns ['Ashley', 'Matt', 'Michael']

print()
print("_________________________________________")
print()

friends = ['ashley', 'matt', 'michael']
     
[friend.capitalize() for friend in friends]

print()
print("_________________________________________")
print()
