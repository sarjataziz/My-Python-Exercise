from csv import DictWriter

with open("example.csv", "w") as file:
	headers = ["Character", "Move"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
			"Character": "Ryu",
			"Move": "Hadouken"
		})