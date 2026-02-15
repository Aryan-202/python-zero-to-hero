"""
Module 05: File Handling & Exceptions - Exercises

Practice reading/writing files and handling errors.
"""

# ==============================================================================
# Exercise 1: Write to File
# ==============================================================================
# Write a function `write_shopping_list` that takes a list of items
# and writes them to a file named "shopping_list.txt", one item per line.

def write_shopping_list(items):
    pass # Your code here

# Test
# items = ["Apples", "Bananas", "Milk", "Bread"]
# write_shopping_list(items)


# ==============================================================================
# Exercise 2: Read and Count
# ==============================================================================
# Write a function `count_lines` that reads "shopping_list.txt"
# and returns the number of lines (items) in the file.
# Handle the FileNotFoundError case by returning 0 and printing a message.

def count_lines(filename):
    pass # Your code here

# Test
# print(f"Items: {count_lines('shopping_list.txt')}")
# print(f"Items: {count_lines('non_existent.txt')}")


# ==============================================================================
# Exercise 3: Safe Division
# ==============================================================================
# Write a function `safe_divide` that takes two numbers and returns the result using division.
# Use a try-except block to handle:
# 1. ZeroDivisionError (print "Cannot divide by zero")
# 2. TypeError (print "Inputs must be numbers")
# Return None if an error occurs.

def safe_divide(a, b):
    pass # Your code here

# Test
# print(safe_divide(10, 2))  # 5.0
# print(safe_divide(5, 0))   # None
# print(safe_divide("a", 2)) # None
