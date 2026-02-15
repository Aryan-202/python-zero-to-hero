"""
Module 07: Advanced Concepts
"""

print("🚀 Module 07: Advanced Concepts")
print("=" * 50)

# List Comprehensions
print("\n1. List Comprehensions")
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(f"Original: {numbers}")
print(f"Squares: {squares}")

# Decorators
print("\n2. Decorators")
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()
