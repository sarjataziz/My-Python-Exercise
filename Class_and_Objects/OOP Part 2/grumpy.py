class GrumpyDict(dict):
	def __repr__(self):
		print("None Of Your Business")
		return super().__repr__() 

	def __missing__(self, key):
		print(f"Toy Want {key}? Well It Ain't Here!")

	def __setitem__(self, key, value):
		print("You Want To Change The Dictionary?")
		print("OK... FINE...")
		super().__setitem__(key, value)

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data["city"] = "Dhaka"
print(data)