"""
Module 07: Advanced Concepts - Exercises
"""

# ==============================================================================
# Exercise 1: List Comprehension
# ==============================================================================
# Use a list comprehension to create a list of numbers from 0 to 20
# that are divisible by both 2 and 3 (e.g., 0, 6, 12, 18).

def get_divisible_by_2_and_3():
    # return [x for ...]
    pass

# Test
# print(get_divisible_by_2_and_3())


# ==============================================================================
# Exercise 2: Lambda Sort
# ==============================================================================
# Given a list of students: [{"name": "Alice", "score": 88}, {"name": "Bob", "score": 95}, {"name": "Charlie", "score": 78}]
# Sort them by SCORE in descending order using a lambda function as the key.

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 78}
]

def sort_students(student_list):
    # return sorted(...)
    pass

# Test
# print(sort_students(students))


# ==============================================================================
# Exercise 3: Simple Decorator
# ==============================================================================
# Write a decorator `make_bold` that wraps the returned string of a function in HTML bold tags <b>...</b>.

def make_bold(func):
    pass

@make_bold
def get_message():
    return "Hello World"

# Test
# print(get_message())  # Should print "<b>Hello World</b>"
