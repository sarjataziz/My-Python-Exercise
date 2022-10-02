#shopping cart

cart = [{"Name": "Box", "Quantity": 3, "Price": 1000}]
print(cart)

#cat

cat = {"Name": "Blue", "Age": 3.5}
print(cat)

#using dict()

a = dict(name = "AB", age = 5)
print(a)

print(cat["Name"])  #"Name": "Box"

print("__________________________")


for val in cat.values():
	print(val)                       #print = Blue , 3.5

print("__________________________")


for v in a.keys():
	print(v)                          #print = name, age

print("__________________________")

for k,v in a.items():
	print(f"key is {k} and values is {v}")

print("__________________________")


new_user = {}.fromkeys(["Name", "Score", "Email", "Profile"], "unknown")
print(new_user)

print("__________________________")

