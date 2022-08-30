class User:

	active_users = 0

	@classmethod
	def display_active_users(cls):
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

class Moderator(User):
	total_moderators = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_moderators += 1

	@classmethod
	def display_active_moderators(cls):
		return f"There are currently {cls.total_moderators} active Moderators"

	def remove_post(self):
		return f"{self.full_name()} remove a post from the {self.community} community"

user1 = User("Ahj", "Gkl", 12)
user2 = User("Ahj", "Gkl", 12)
user3 = User("Ahj", "Gkl", 12)
user4 = User("Ahj", "Gkl", 12)
roger = Moderator("Gol D.", "Roger", 46, "Roger Pirate")
print(User.display_active_users())
print(Moderator.display_active_moderators())


