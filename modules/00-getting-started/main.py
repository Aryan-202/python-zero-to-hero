"""
Module 00: Getting Started with Python

This file contains the main content for the Getting Started module.
Follow along with the examples and run the code to see Python in action!
"""

print("🎉 Welcome to Python Programming!")
print("=" * 40)

# ==============================================================================
# 1. WHAT IS PYTHON?
# ==============================================================================

print("\n1. WHAT IS PYTHON?")
print("-" * 20)

print("Python is a versatile programming language used for:")
python_uses = [
    "Web Development",
    "Data Science & Analysis", 
    "Artificial Intelligence",
    "Automation & Scripting",
    "Game Development",
    "Scientific Computing"
]

for i, use in enumerate(python_uses, 1):
    print(f"   {i}. {use}")

# ==============================================================================
# 2. YOUR FIRST PYTHON PROGRAM
# ==============================================================================

print("\n2. YOUR FIRST PYTHON PROGRAM")
print("-" * 30)

# The classic first program
print("Hello, World!")

# Python can do math
print("\nPython can do calculations:")
print(f"2 + 3 = {2 + 3}")
print(f"10 * 5 = {10 * 5}")
print(f"100 / 4 = {100 / 4}")

# ==============================================================================
# 3. VARIABLES AND BASIC OPERATIONS
# ==============================================================================

print("\n3. VARIABLES AND BASIC OPERATIONS")
print("-" * 35)

# Variables store data
name = "Alice"
age = 25
temperature = 98.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Temperature: {temperature}")
print(f"Is student: {is_student}")

# You can perform operations with variables
birth_year = 2024 - age
print(f"\nIf {name} is {age} years old, they were born around {birth_year}")

# ==============================================================================
# 4. BASIC INPUT AND OUTPUT
# ==============================================================================

print("\n4. BASIC INPUT AND OUTPUT")
print("-" * 30)

# Getting input from user
# Uncomment the lines below to try user input:
# user_name = input("What's your name? ")
# print(f"Hello, {user_name}! Welcome to Python!")

# ==============================================================================
# 5. COMMENTS AND DOCUMENTATION
# ==============================================================================

print("\n5. COMMENTS AND DOCUMENTATION")
print("-" * 35)

# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines and is often used
for documentation at the top of files.
"""

# Comments are essential for:
# - Explaining complex code
# - Leaving notes for yourself or others
# - Temporarily disabling code

def example_function():
    """
    This is a docstring - it documents what the function does.
    
    Returns:
        str: A welcome message
    """
    return "This function returns a welcome message"

# ==============================================================================
# 6. GETTING HELP
# ==============================================================================

print("\n6. GETTING HELP")
print("-" * 20)

print("When you need help in Python:")
help_sources = [
    "Use help() function: help(print)",
    "Use dir() to see available methods: dir(str)",
    "Python official documentation",
    "Stack Overflow for specific questions",
    "This course's resources!"
]

for i, source in enumerate(help_sources, 1):
    print(f"   {i}. {source}")

# Let's try the help function
print("\nTrying help function on print:")
# help(print)  # Uncomment to see the help for print function

# ==============================================================================
# 7. PYTHON SYNTAX BASICS
# ==============================================================================

print("\n7. PYTHON SYNTAX BASICS")
print("-" * 25)

print("Python uses indentation to define code blocks:")
print("""
if True:
    print("This is indented")
    print("So is this")
print("This is not indented")
""")

print("Key syntax rules:")
syntax_rules = [
    "Indentation matters (use 4 spaces)",
    "Variables don't need type declarations",
    "Function definitions use 'def'",
    "Comments start with #",
    "Strings can use 'single' or \"double\" quotes"
]

for rule in syntax_rules:
    print(f"   • {rule}")

# ==============================================================================
# 8. PRACTICE EXAMPLES
# ==============================================================================

print("\n8. PRACTICE EXAMPLES")
print("-" * 20)

# Example 1: String manipulation
message = "python programming"
print(f"Original: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Title case: {message.title()}")

# Example 2: Number operations
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"\nCircle with radius {radius}:")
print(f"Area = π × r² = {area:.2f}")

# Example 3: Boolean logic
can_vote = age >= 18
print(f"\n{name} can vote: {can_vote}")

# ==============================================================================
# NEXT STEPS
# ==============================================================================

print("\n" + "=" * 50)
print("NEXT STEPS")
print("=" * 50)

print("""
Great job completing the introduction! 🎉

Next, you should:
1. Complete the exercises in exercises.py
2. Check your solutions with solutions.py  
3. Take the quiz in quiz.py
4. Move on to Module 01: Variables and Data Types

Remember:
- Practice regularly
- Don't be afraid to experiment
- Ask for help when needed
- Most importantly: HAVE FUN! 🐍
""")

# Final encouraging message
print("\n🚀 You're on your way to becoming a Python programmer!")