"""
Module 02: Control Flow - Solutions

These are the solutions to the exercises in exercises.py.
"""

print("--- Module 02 Solutions ---")

# ==============================================================================
# Exercise 1: Grade Calculator
# ==============================================================================
print("\nExercise 1: Grade Calculator")

score = 85
grade = ""

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")


# ==============================================================================
# Exercise 2: Even or Odd
# ==============================================================================
print("\nExercise 2: Even or Odd")

number = 42

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")


# ==============================================================================
# Exercise 3: Sum of First N Numbers
# ==============================================================================
print("\nExercise 3: Sum of First N Numbers")

n = 10
sum_n = 0

for i in range(1, n + 1):
    sum_n += i

print(f"Sum of numbers from 1 to {n} is: {sum_n}")


# ==============================================================================
# Exercise 4: Multiplication Table
# ==============================================================================
print("\nExercise 4: Multiplication Table")

num = 7

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")


# ==============================================================================
# Exercise 5: Find the Factorial
# ==============================================================================
print("\nExercise 5: Find the Factorial")

limit = 5
current = limit
factorial = 1

while current > 0:
    factorial *= current
    current -= 1

print(f"Factorial of {limit} is: {factorial}")
