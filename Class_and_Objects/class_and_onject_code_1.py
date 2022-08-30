class Person:
	def __init__(self):
		self.name = "Aziz"
		self._secret = "hi"
		self.__msg = "Hello..."

p = Person()
print(p.name)
print(p._secret)
print(p._Person__msg)