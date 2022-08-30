from csv import reader

with open("fighters.csv") as file:
	cvs_reader = reader(file)
	for fighter in cvs_reader:
		print(f"{fighter[0]} is from {fighter[1]}")
		#print(row)