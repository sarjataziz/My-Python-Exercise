from csv import writer

with open("Testing.csv", "w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Name", "Age"])
	csv_writer.writerow(["Ryu", 20])
	csv_writer.writerow(["Keu", 34])
	csv_writer.writerow(["Yue", 19])
	csv_writer.writerow(["Ilas", 23])
	csv_writer.writerow(["Pkhs", 28])
	csv_writer.writerow(["Rkho", 18])
	csv_writer.writerow(["Gkjh", 25])
