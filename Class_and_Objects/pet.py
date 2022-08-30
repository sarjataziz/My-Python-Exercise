class Pet:
	allowed = ["cat", "dog", "fish", "rat", "bunny", "bird"]
	def __init__(self, name, species):
		if species not in self.allowed:
			raise ValueError(f"You can't have a {species} pet")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in self.allowed:
			raise ValueError(f"You can't have a {species} pet")
		self.species = species

cat = Pet("Rabbi", "cat")
dog = Pet("Ka", "dog")

print(cat)
print(dog)