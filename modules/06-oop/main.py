"""
Module 06: Object-Oriented Programming (OOP)
"""

print("🏗️ Module 06: OOP")
print("=" * 50)

# Defining a Class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating Objects
my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog consists of: {my_dog.name}, Breed: {my_dog.breed}")
print(my_dog.bark())

# Inheritance
class Puppy(Dog):
    def bark(self):
        return f"{self.name} says Yip!"

specs = Puppy("Spot", "Dalmatian")
print(f"Puppy: {specs.bark()}")
