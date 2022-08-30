from random import random

def flip_coin():
	r = random()
	if r > 0.5:
		return "Head"
	else:
		return "Tail"

#print(flip_coin())

def flip_coin():
	if random() > 0.5:
		return "HEAD"
	else:
		return "TAIL"
print(flip_coin())
