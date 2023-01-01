class Dog(object):
	"""A simple attempt to model a dog"""
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age


	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(f"{self.name} is now sitting.")


	def roll_over(self):
		"""Simulate a dog rolling over in response to a commmand"""
		print(f"{self.name} is now rolling over.")


my_dog = Dog("Willie", 6)  # instantiation
print(f"My dog's name is {my_dog.name}.")  # accessing attributes
print(f"My dog is {my_dog.age} years old.")

print()
print(my_dog.sit())
print(my_dog.roll_over())

print()
your_dog = Dog("Lucy", 3)  # instantiation
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
print(your_dog.sit())
print(your_dog.roll_over())


