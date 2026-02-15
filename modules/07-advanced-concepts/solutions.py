"""
Module 07: Advanced Concepts - Solutions
"""

print("--- Module 07 Solutions ---")

# ==============================================================================
# Exercise 1: List Comprehension
# ==============================================================================
print("\nExercise 1: List Comprehension")

def get_divisible_by_2_and_3():
    return [x for x in range(21) if x % 2 == 0 and x % 3 == 0]

print(f"Divisible by 2 and 3 (0-20): {get_divisible_by_2_and_3()}")


# ==============================================================================
# Exercise 2: Lambda Sort
# ==============================================================================
print("\nExercise 2: Lambda Sort")

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 78}
]

# Sort by score descending
sorted_students = sorted(students, key=lambda s: s['score'], reverse=True)
print("Sorted students:", sorted_students)


# ==============================================================================
# Exercise 3: Simple Decorator
# ==============================================================================
print("\nExercise 3: Simple Decorator")

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

@make_bold
def get_message():
    return "Hello World"

print(get_message())
