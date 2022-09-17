from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number <= 10:
    i += i
    if number == 5:
        print(number)
        break
        
