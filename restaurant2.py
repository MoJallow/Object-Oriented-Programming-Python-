class Restaurant(object):
    """Attempts to model a simple restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the attributes to describe a restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 5

    def describe_restaurant(self):
        """Returns a neatly formatted description of a restaurant"""
        print(f"{self.name.title()}: {self.cuisine_type.title()}")
        
    def open_restaurant(self):
        """Prints restaurant is open."""
        print(f"{self.name.title()} is open!")
        
    def set_number_served(self, new_number):
        """updates the number of customers served"""
        self.number_served = new_number
        
    def increment_number_served(self, add_number):
        """Add value to the existing number served."""
        self.number_served += add_number
        
restaurant = Restaurant("Hazel Restaurant", "Pizza")
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(25)
print(restaurant.number_served)
