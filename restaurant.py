class Restaurant(object):
	"""models a simple restaurant"""
	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		"""prints the name and cuisine type offered at the restaurant"""
		print(f"Restaurant: {self.name}")
		print(f"Cuisine type: {self.cuisine_type}")



	def open_restaurant(self):
		"""Gives status of the restaurant"""
		print("Status: OPEN")


restaurant_one = Restaurant("Sambou's Restaurant", "Jollof Rice")

print(f"The name of the restaurant is {restaurant_one.name}.")
print(f"Cuisine type offered at the restaurant is {restaurant_one.cuisine_type}.")

print(restaurant_one.describe_restaurant())
print(restaurant_one.open_restaurant())

print()

restaurant_two = Restaurant("Doudou's Restaurant", "Sea-foods")
print(f"The name of the restaurant is {restaurant_two.name}.")
print(f"Cuisine type offered at the restaurant is {restaurant_one.cuisine_type}.")

print(restaurant_two.describe_restaurant())
print(restaurant_two.open_restaurant())

