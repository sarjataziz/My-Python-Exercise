
for number in range(1,21):
    if number == 4 or number == 13:
        print(f"{number} : Unlucky!")
    elif number % 2 == 0:
        print(f"{number} : is Even")
    else:
        print(f"{number} : is Odd")

print()
print("______________________________________")
print("======================================")
print()

for number in range(1,21):
    if number == 4 or number == 13:
        state = "unlucky"
    elif number % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{number} : is {state}")
