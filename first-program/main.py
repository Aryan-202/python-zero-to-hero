"""
First Python Program - Hello World and Basic Concepts
Course: Learn Python - GitHub Open Source
Author: Your Name
"""

# =============================================================================
# SECTION 1: BASIC OUTPUT AND COMMENTS
# =============================================================================

# This is a single-line comment
print("=== WELCOME TO PYTHON PROGRAMMING! ===")
print("Hello, World! 🌍")  # This prints text to the console

"""
This is a multi-line comment.
It can span multiple lines and is useful for documentation.
We're learning the basics of Python programming!
"""

# =============================================================================
# SECTION 2: BASIC ARITHMETIC OPERATIONS
# =============================================================================

print("\n=== BASIC ARITHMETIC ===")

# Addition
result_add = 5 + 3
print(f"5 + 3 = {result_add}")

# Subtraction
result_sub = 10 - 4
print(f"10 - 4 = {result_sub}")

# Multiplication
result_mul = 6 * 7
print(f"6 * 7 = {result_mul}")

# Division
result_div = 15 / 3
print(f"15 / 3 = {result_div}")

# Integer Division (floor division)
result_int_div = 17 // 5
print(f"17 // 5 = {result_int_div}")

# Modulus (remainder)
result_mod = 17 % 5
print(f"17 % 5 = {result_mod}")

# Exponentiation
result_exp = 2 ** 4
print(f"2 ** 4 = {result_exp}")

# =============================================================================
# SECTION 3: STRING OPERATIONS
# =============================================================================

print("\n=== STRING OPERATIONS ===")

# String concatenation
greeting = "Hello" + " " + "Python"
print(greeting)

# String repetition
laugh = "Ha" * 3
print(f"Laughter: {laugh}")

# String methods
name = "python programmer"
print(f"Original: {name}")
print(f"Uppercase: {name.upper()}")
print(f"Title case: {name.title()}")

# String formatting (f-strings)
language = "Python"
version = 3.12
print(f"I'm learning {language} version {version}!")

# =============================================================================
# SECTION 4: USER INPUT
# =============================================================================

print("\n=== USER INPUT ===")

# Getting input from user
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")

# Converting input to numbers
age = input("How old are you? ")
# Note: input() always returns a string, so we need to convert it
age_number = int(age)
print(f"Next year, you'll be {age_number + 1} years old!")

# =============================================================================
# SECTION 5: BASIC PROGRAM FLOW
# =============================================================================

print("\n=== PROGRAM FLOW ===")

# Simple if statement
temperature = 25

if temperature > 30:
    print("It's a hot day! ☀️")
elif temperature > 20:
    print("Perfect weather! 😊")
else:
    print("It's a bit cold! ❄️")

# =============================================================================
# SECTION 6: FUNCTIONS - YOUR FIRST FUNCTION
# =============================================================================

print("\n=== FUNCTIONS ===")


def greet_person(name, time_of_day="day"):
    """
    This function greets a person based on the time of day.

    Parameters:
    name (str): The person's name
    time_of_day (str): Time of day (morning, afternoon, evening)

    Returns:
    str: A greeting message
    """
    return f"Good {time_of_day}, {name}! 👋"


# Using the function
greeting1 = greet_person("Alice", "morning")
greeting2 = greet_person("Bob")  # Uses default value
print(greeting1)
print(greeting2)

# =============================================================================
# SECTION 7: LISTS - BASIC COLLECTIONS
# =============================================================================

print("\n=== LISTS ===")

# Creating a list
fruits = ["apple", "banana", "orange", "grape"]
print(f"My favorite fruits: {fruits}")

# Accessing list elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Adding to list
fruits.append("strawberry")
print(f"After adding strawberry: {fruits}")

# =============================================================================
# SECTION 8: PUTTING IT ALL TOGETHER - MINI PROJECT
# =============================================================================

print("\n=== MINI PROJECT: SIMPLE CALCULATOR ===")


def simple_calculator():
    """A simple calculator that performs basic operations"""
    print("\n🧮 SIMPLE CALCULATOR")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operation!")
            return

        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Please enter valid numbers!")


# Run the calculator
simple_calculator()

# =============================================================================
# SECTION 9: PROGRAM EXECUTION INFORMATION
# =============================================================================

print("\n" + "=" * 50)
print("🎉 CONGRATULATIONS! 🎉")
print("You've completed your first Python program!")
print("This program covered:")
print("✓ Basic output and comments")
print("✓ Arithmetic operations")
print("✓ String manipulation")
print("✓ User input")
print("✓ Conditional statements")
print("✓ Functions")
print("✓ Lists")
print("✓ Error handling")
print("=" * 50)

# Display Python version info (bonus)
import sys

print(f"\nPython version: {sys.version}")
print("Keep learning and coding! 🚀")