class Human(object):
	"""docstring for Human"""
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self.age = age
		else:
			self.age = 0
	'''def get_age(self):
		return self.get_age

	def set_age(self, new_age):
		if new_age >= 0:
			self._age = new_age
		else:
			self._age = 0'''

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			self._age = 0
	

a = Human("Gol D. ", "Roger", 46)
print(a.age)
		