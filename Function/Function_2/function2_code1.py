def sum_all_num(*args):
	total = 0
	for num in args:
		total += num 
	return total

print(sum_all_num(1,3,2,5,1))
print(sum_all_num(24321,1243))


def fav_colors(**kwargs):
	print(kwargs)
fav_colors(sarjat = "Blue")

def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(kwargs)
fav_colors(sarjat = "Blue")

def special_greeting(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "You get a special greeeting David"
	elif "David" in kwargs:
		return f"{kwargs['David']} David"
	return "Not sure who this is...."

print(special_greeting(David = "Hello"))
print(special_greeting(Bob = "Hello"))
print(special_greeting(David = "special"))
