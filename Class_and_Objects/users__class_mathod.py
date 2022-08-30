class User:

	active_users = 0

	@classmethod
	def display_Active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

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

user_1 = User.from_string("Tbhj,Ubhjg,100")
user_2 = User.from_string("Nlkla,Akfsjh,10")

print(user_2.full_name())
print(user_1.likes("Ice Cream"))
print(user_2.likes("Chips"))
print(user_1.first, user_1.last, user_1.age)
#print(user_2.first, user_2.last, user_2.age)
print(user_2.birthday())
print(user_1.birthday())

print(user_2.logout())
print(User.active_users)