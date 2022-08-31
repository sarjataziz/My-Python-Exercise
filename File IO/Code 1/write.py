'''with open("haiku.txt", "w") as file:
	file.write("Writing file is great..")'''

'''with open("haiku.txt", "a") as file:
	file.write("file is great..")'''

with open("haiku.txt", "r+") as file:
	file.write("\n Add")
	
