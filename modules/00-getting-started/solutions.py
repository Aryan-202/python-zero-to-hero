"""
Module 00: Getting Started - Solutions

These are the solutions for the exercises in this module.
Try to solve the exercises yourself before looking here!
"""

# ==============================================================================
# EXERCISE 1: Hello, Python!
# ==============================================================================

def exercise_1():
    """
    Write a program that prints:
    - "Hello, Python!" on the first line
    - "I'm excited to learn programming!" on the second line
    - Your name on the third line
    """
    print("Hello, Python!")
    print("I'm excited to learn programming!")
    print("Alice")  # Replace with your name

# ==============================================================================
# EXERCISE 2: Basic Calculations
# ==============================================================================

def exercise_2():
    """
    Calculate and print the results of:
    - 15 + 7
    - 30 - 12
    - 6 * 8
    - 45 / 9
    - 2 ** 5 (2 to the power of 5)
    """
    print("15 + 7 =", 15 + 7)
    print("30 - 12 =", 30 - 12)
    print("6 * 8 =", 6 * 8)
    print("45 / 9 =", 45 / 9)
    print("2 ** 5 =", 2 ** 5)

# ==============================================================================
# EXERCISE 3: Variable Practice
# ==============================================================================

def exercise_3():
    """
    Create variables to store:
    - Your favorite book title
    - The year it was published
    - How many times you've read it
    - Whether you would recommend it (True/False)
    
    Then print a message using these variables.
    """
    book_title = "The Python Guide"
    publish_year = 2020
    times_read = 3
    would_recommend = True
    
    print(f"My favorite book is '{book_title}' published in {publish_year}.")
    print(f"I've read it {times_read} times and would recommend it: {would_recommend}")

# ==============================================================================
# EXERCISE 4: String Operations
# ==============================================================================

def exercise_4():
    """
    Create a variable with your favorite programming language.
    Then print:
    - The language in uppercase
    - The language in lowercase
    - The length of the language name
    - The first 3 letters of the language name
    """
    language = "Python"
    
    print("Uppercase:", language.upper())
    print("Lowercase:", language.lower())
    print("Length:", len(language))
    print("First 3 letters:", language[:3])

# ==============================================================================
# EXERCISE 5: Temperature Converter
# ==============================================================================

def exercise_5():
    """
    Convert 100 degrees Fahrenheit to Celsius using the formula:
    Celsius = (Fahrenheit - 32) * 5/9
    
    Print both temperatures with clear labels.
    """
    fahrenheit = 100
    celsius = (fahrenheit - 32) * 5/9
    
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# ==============================================================================
# EXERCISE 6: User Input (Bonus)
# ==============================================================================

def exercise_6():
    """
    Ask the user for their:
    - Favorite color
    - Favorite number
    
    Then print a message incorporating their answers.
    """
    color = input("What's your favorite color? ")
    number = input("What's your favorite number? ")
    print(f"Your favorite color is {color} and favorite number is {number}!")

# ==============================================================================
# EXERCISE 7: Simple Mad Lib
# ==============================================================================

def exercise_7():
    """
    Create a simple mad lib story that uses:
    - A name
    - An animal
    - A verb
    - An adjective
    
    Print the completed story.
    Example: "Sarah has a cute dog that loves to run quickly."
    """
    name = "Alex"
    animal = "cat"
    verb = "sleep"
    adjective = "playful"
    
    story = f"{name} has an {adjective} {animal} that loves to {verb} all day."
    print(story)

# ==============================================================================
# EXERCISE 8: Math Operations
# ==============================================================================

def exercise_8():
    """
    Calculate and print:
    - The area of a rectangle with width 8 and height 12
    - The circumference of a circle with radius 10 (2 * π * radius)
    - The remainder when 27 is divided by 4
    """
    import math
    
    # Rectangle area
    width = 8
    height = 12
    area = width * height
    print(f"Rectangle area: {width} * {height} = {area}")
    
    # Circle circumference
    radius = 10
    circumference = 2 * math.pi * radius
    print(f"Circle circumference: 2 * π * {radius} = {circumference:.2f}")
    
    # Remainder
    remainder = 27 % 4
    print(f"27 % 4 = {remainder}")

# ==============================================================================
# EXERCISE 9: Boolean Logic
# ==============================================================================

def exercise_9():
    """
    Create variables for:
    - A person's age
    - Whether they have a driver's license (True/False)
    
    Determine and print if they can:
    - Vote (18 or older)
    - Drive (has license and 16 or older)
    """
    age = 20
    has_license = True
    
    can_vote = age >= 18
    can_drive = has_license and age >= 16
    
    print(f"Age: {age}")
    print(f"Has license: {has_license}")
    print(f"Can vote: {can_vote}")
    print(f"Can drive: {can_drive}")

# ==============================================================================
# EXERCISE 10: Formatting Practice
# ==============================================================================

def exercise_10():
    """
    Create a nicely formatted bio that includes:
    - Name
    - Age
    - Occupation
    - Hobby
    
    Format it so each item is on a new line with clear labels.
    """
    name = "Jordan"
    age = 28
    occupation = "Software Developer"
    hobby = "photography"
    
    print("Personal Bio:")
    print("-------------")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Occupation: {occupation}")
    print(f"Hobby: {hobby}")

# ==============================================================================
# MAIN FUNCTION TO RUN ALL SOLUTIONS
# ==============================================================================

def main():
    """
    Run all exercise solutions in sequence.
    """
    print("Module 00 Exercise Solutions")
    print("=" * 30)
    
    exercises = [
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
        exercise_6, exercise_7, exercise_8, exercise_9, exercise_10
    ]
    
    for i, exercise in enumerate(exercises, 1):
        print(f"\nExercise {i}:")
        print("-" * 12)
        exercise()

if __name__ == "__main__":
    main()