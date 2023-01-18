class User(object):
    """Models user profile behavior"""

    def __init__(self, first_name, last_name, gender, eye_color, birth_date, address, phone, email):
        """Initialize all the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.eye_color = eye_color
        self.birth_date = birth_date
        self.address = address
        self.phone = phone
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """summarizes user information"""
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Eye Color: {self.eye_color}")
        print(f"Date of Birth: {self.birth_date}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """sends greetings to user"""
        print(f"Hello, {self.first_name} {self.last_name}!")


    def increment_login_attempts(self):
        """increases the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset number of login attempts to zero."""
        self.login_attempts = 0
        
        
user1 = User("Muhammad", "Galleh", "M", "Brown", 20001, "Kartong", "07988", "user1@xxx.com")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
