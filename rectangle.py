class Rectangle(object):
	def __init__(self, color, length, width):
		self.color = color
		self.length = length
		self.width = width

	
	def area(self):
		self.area = self.length * self.width
		return self.area


	def perimeter(self):
		self.perimeter = 2 * (self.length + self.width)
		return self.perimeter


	def diagonal(self):
		self.diagonal = (self.length ** 2 + self.width ** 2) ** (1/2)
		return self.diagonal


	def volume(self, height):
		self.volume = self.length * self.width * height
		return self.volume


rectangle_1 = Rectangle("red", 4, 3)
print(rectangle_1.color)
print(rectangle_1.length)
print(rectangle_1.width)
print(rectangle_1.area())
print(rectangle_1.perimeter())
print(rectangle_1.diagonal())
print(rectangle_1.volume(5))

print()

rectangle_2 = Rectangle("blue", 8, 4.5)
print(rectangle_2.color)
print(rectangle_2.length)
print(rectangle_2.width)
print(rectangle_2.area())
print(rectangle_2.perimeter())
print(rectangle_2.diagonal())
print(rectangle_2.volume(9.5))
