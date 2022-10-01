# # num_char = len(input("What's your name?"))
# # new_num_char = str(num_char)
# # print("Yor name contains " + new_num_char + " characters")
# # print(70 + float(124.14))
# print(type(input()))
# 
print("Welcome to the rollercoster")
height = int(input("What is your height in cm? \n"))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill =7
        print("Youth tickets are $7.")
    else:
        bill =12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N.\n")
    if wants_photo == "Y":
        bill += 3     
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")
    
