"""
Module 03: Functions and Modules - Solutions
"""

import math

print("--- Module 03 Solutions ---")

# ==============================================================================
# Exercise 1: Calculate Area
# ==============================================================================
print("\nExercise 1: Calculate Area")

def calculate_area(radius):
    return math.pi * (radius ** 2)

r = 5
print(f"Area of circle with radius {r}: {calculate_area(r):.2f}")


# ==============================================================================
# Exercise 2: Temperature Converter
# ==============================================================================
print("\nExercise 2: Temperature Converter")

def celsius_to_fahrenheit(celsius=0):
    return (celsius * 9/5) + 32

print(f"25°C in Fahrenheit: {celsius_to_fahrenheit(25)}")
print(f"0°C (default) in Fahrenheit: {celsius_to_fahrenheit()}")


# ==============================================================================
# Exercise 3: Is Palindrome
# ==============================================================================
print("\nExercise 3: Is Palindrome")

def is_palindrome(word):
    # Convert to lowercase and remove spaces for robustness (optional but good practice)
    clean_word = word.lower().replace(" ", "")
    return clean_word == clean_word[::-1]

print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
print(f"Is 'hello' a palindrome? {is_palindrome('hello')}")


# ==============================================================================
# Exercise 4: Max of Three
# ==============================================================================
print("\nExercise 4: Max of Three")

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"Max of 10, 5, 8 is: {find_max(10, 5, 8)}")
print(f"Max of 1, 99, 2 is: {find_max(1, 99, 2)}")
