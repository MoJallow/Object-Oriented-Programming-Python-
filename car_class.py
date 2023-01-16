class Car(object):
	"""A simple attempt to represent a car."""

	def __init__(self, maker, model, year):
		"""Initialize attributes to describe a car."""
		self.maker = maker
		self.model = model
		self.year = year


	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		return f"{self.year} {self.maker} {self.model}"


my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_descriptive_name())