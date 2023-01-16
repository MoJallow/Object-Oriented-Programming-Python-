class Car(object):
    "A simple attempt to represent a car"
    
    def __init__(self, manufacturer, model, year):
        "Initialize attributes to describe a car"
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0  # set a default value for an attribute
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        return f"{self.manufacturer.title()} {self.model.title()} {self.year}"
    
    
    def read_odometer(self):
        """Prints a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())

# modify attribute value directly
my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())
        
        
        