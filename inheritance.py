class Car(object):  # Parent class
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
        
     # modify attribute value using method   
    def update_odometer_reading(self, mileage):
        """
        set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer reading back!
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer_reading(self, miles):
        """Increment odometer to new value"""
        self.odometer_reading += miles
    
    

class ElectricCar(Car):  # child class
    """Represents aspects of a car, specific to electric cars."""
    
    def __init__(self, manufacturer, model, year):
        """Initializes attributes of the parent class."""
        super().__init__(manufacturer, model, year)
        
        
my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
