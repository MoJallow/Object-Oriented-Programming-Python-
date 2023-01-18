class Team(object):
    """Attempts to model a football team in a season."""
    def __init__(self, name, year, city):
        """Initialize attributes to describe a football team."""
        self.name = name
        self.year = year
        self.city = city
        self.points = 0
        
    def team_details(self):
        """Returns a neatly formatted details of the team"""
        print(f"Name:{self.name.title().strip()}")
        print(f"Est:{self.year}")
        print(f"City:{self.city.title()}")
        
    def read_points(self):
        """Return a neatly formatted outputs of the team's point."""
        print(f"{self.name.title()} has {self.points} points.")
        
    def update_points(self, new_points):
        """
        Set points to the given value.
        Reject any attempt to roll back points
        """
        if new_points >= self.points:
            self.points = new_points
        else:
            print("You can't roll back points!")
            
            
    def increment_points(self, pts):
        """Adds new points to the existing points """
        self.points += pts
        
        
my_team = Team("liverpool football club", 1879, "liverpool")
print(my_team.team_details())
print(my_team.read_points())
my_team.update_points(15)
print(my_team.read_points())
my_team.update_points(10)  #displays you can't roll back points!
my_team.increment_points(3)  # increase the existing point by 3
print(my_team.read_points())