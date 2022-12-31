class Customer(object):
	def __init__(self, name, membership_type):
		self.name = name
		self.membership_type = membership_type

#customer_1 = Customer("Sam", "Gold")  # instantiation
#print(f"{customer_1.name}, {customer_1.membership_type}")

#customer_2 = Customer("Harry", "Platinum")
#print(f"{customer_2.name}, {customer_2.membership_type}")

customers = [
				Customer("Sam", "Gold"),
				Customer("Harry", "Platinum"),
				Customer("Tima", "Bronze")
				]

for customer in customers:
	print(f"{customer.name}, {customer.membership_type}")