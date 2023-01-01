class User(object):
	"""Models user profile behavior"""
	def __init__(self, first_name, last_name, gender, eye_color, birth_date, address, phone , email):
		"""Initialize all the attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender 
		self.eye_color = eye_color
		self.birth_date = birth_date
		self.address = address
		self.phone = phone
		self.email = email


	def describe_user(self):
		"""summarizes user information"""
		print(f"First name: {self.first_name}")
		print(f"Last name: {self.last_name}")
		print(f"Gender: {self.gender}")
		print(f"Eye Color: {self.eye_color}")
		print(f"Date of Birth: {self.birth_date}")
		print(f"Address: {self.address}")
		print(f"Phone: {self.phone}")
		print(f"Email: {self.email}")


	def greet_user(self):
		"""sends greetings to user"""
		print(f"Hello, {self.first_name} {self.last_name}!")





# Instantiation
user_1 = User("Sam", "Giggs", "Male", "Black", "09-05-22", "Mukono", "(+256)755987321", "user1@gmail.com")

print(user_1.describe_user())
print(user_1.greet_user())

print()

user_2  = User("Rohey", "Galleh", "Female", "Brown", "04-22-2001", "Kartong", "(+220)3126247", "user2@gmail.com")

print(user_2.describe_user())
print(user_2.greet_user())