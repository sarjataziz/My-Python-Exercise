def get(d,key):
	try:
		return d[key]
	except keyError:
		return None

d = {"Name": "Aziz"}
print(get(d,"city"))
print(get(d,"Name"))