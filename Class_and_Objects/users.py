class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

user_1 = User("Tbhj", "Ubhjg", 100)
user_2 = User("Nlkla", "Akfsjh", 10)

print(user_2.full_name())
print(user_1.likes("Ice Cream"))
print(user_2.likes("Chips"))
print(user_1.first, user_1.last, user_1.age)
print(user_2.first, user_2.last, user_2.age)
print(user_2.initials())
print(user_1.initials())
print(user_2.is_senior())
print(user_1.is_senior())
print(user_2.birthday())
print(user_1.birthday())
