# Define a class for a simple Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("Alice", 30)
person1.greet()
