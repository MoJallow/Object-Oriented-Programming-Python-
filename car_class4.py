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
    
    
my_new_car = Car("bmw", "a4", 2019)
print(my_new_car.odometer_reading)
my_new_car.update_odometer_reading(25)
print(my_new_car.read_odometer())

my_new_car.update_odometer_reading(15)  # displays you can't roll back odometer reading