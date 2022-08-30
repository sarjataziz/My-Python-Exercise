#Define a function called generate_evens
def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]
#It should return a list of even numbers between 1 and 50(not including 50)
print(generate_evens())