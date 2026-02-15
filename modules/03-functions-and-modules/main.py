"""
Module 03: Functions and Modules

This module demonstrates:
- Defining and calling functions
- Arguments and return values
- Variable scope
- Importing and using modules
"""

import random  # Importing a built-in module
import math

print("📦 Module 03: Functions and Modules")
print("=" * 50)

# ==============================================================================
# 1. DEFINING AND CALLING FUNCTIONS
# ==============================================================================

print("\n1. DEFINING AND CALLING FUNCTIONS")
print("-" * 30)

# Basic function
def say_hello():
    print("Hello, World! 🌍")

# Calling the function
print("Calling say_hello():")
say_hello()

# Function with parameters
def greet(name):
    print(f"Hello, {name}! 👋")

print("\nCalling greet():")
greet("Alice")
greet("Bob")


# ==============================================================================
# 2. RETURN VALUES
# ==============================================================================

print("\n2. RETURN VALUES")
print("-" * 30)

def add(a, b):
    return a + b

result = add(5, 3)
print(f"Result of add(5, 3): {result}")

# Multiple return values (returns a tuple)
def get_dimensions():
    length = 10
    width = 5
    return length, width

l, w = get_dimensions()
print(f"Dimensions: {l} x {w}")


# ==============================================================================
# 3. DEFAULT ARGUMENTS AND KWARGS
# ==============================================================================

print("\n3. DEFAULT ARGUMENTS")
print("-" * 30)

def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Buddy")
describe_pet("Whiskers", "cat")
describe_pet(animal_type="hamster", pet_name="Nibbles")  # Keyword arguments


# ==============================================================================
# 4. VARIABLE SCOPE (Local vs Global)
# ==============================================================================

print("\n4. VARIABLE SCOPE")
print("-" * 30)

global_var = "I am global 🌐"

def check_scope():
    local_var = "I am local 🏠"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

check_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would raise an NameError because local_var is not defined here


# ==============================================================================
# 5. LAMBDA FUNCTIONS
# ==============================================================================

print("\n5. LAMBDA FUNCTIONS")
print("-" * 30)

# lambda arguments: expression
square = lambda x: x * x

print(f"Square of 5 using lambda: {square(5)}")

# Using lambda with built-in functions like map()
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared (map): {squared_numbers}")


# ==============================================================================
# 6. MODULES
# ==============================================================================

print("\n6. MODULES")
print("-" * 30)

# Using the 'math' module imported at the top
print(f"Pi is approximately: {math.pi:.4f}")
print(f"Square root of 25: {math.sqrt(25)}")

# Using the 'random' module
random_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_num}")

# Imagine we have a custom module named 'my_utils.py'
# import my_utils
# my_utils.some_function()

print("\n" + "=" * 50)
print("🚀 End of Module 03 Demonstration")
