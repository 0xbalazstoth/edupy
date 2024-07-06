class University:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome to {self.name}, the parent class!")


class Student(University):
    def __init__(self, name, age):
        # Call the constructor of the parent class
        super().__init__(name)  # Szülő teljes tulajdonságainak öröklése
        self.age = age

    def welcome(self):
        # Call the method from the parent class
        super().welcome()
        print(f"I am {self.age} years old, and I am from the child class!")


# Example usage
student = Student("XYZ University", 23)
student.welcome()
