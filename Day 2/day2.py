''' This person class is a simple class that has a name and age attribute. It also has a display method that prints the name and age of the person.'''
""" The validate_person_name method takes in the name as a parameter and checks if the length of the name is greater than 0. If it is, it returns True. If it is not, it returns False."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def validate_person_name(self, name):
        if len(name) > 0:
            return True
        return False
    
    def validate_person_age(self, age):
        if age >= 0:
            return True
        return False
    
    def get_person_name(self):
        return self.name
    
    def get_person_age(self):
        return self.age

    def set_person_name(self, name):
        self.name = name
    
    def set_person_age(self, age):
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}\nAge: {self.age} years old")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p1.display_person()
p2.display_person()
