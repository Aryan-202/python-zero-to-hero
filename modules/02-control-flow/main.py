"""
Module 02: Control Flow

This module demonstrates how to control the flow of execution in Python programs using:
- Conditional Statements (if, elif, else)
- For Loops
- While Loops
- Loop Control (break, continue)
"""

print("🚦 Module 02: Control Flow")
print("=" * 50)

# ==============================================================================
# 1. CONDITIONAL STATEMENTS (if, elif, else)
# ==============================================================================

print("\n1. CONDITIONAL STATEMENTS")
print("-" * 30)

# Basic if statement
age = 20

print(f"Age: {age}")
if age >= 18:
    print("You are an adult. ✅")
else:
    print("You are a minor. 🚫")

# elif statement (else if)
score = 85

print(f"\nScore: {score}")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# Nested if statements
is_weekend = True
is_sunny = False

print(f"\nWeekend: {is_weekend}, Sunny: {is_sunny}")
if is_weekend:
    if is_sunny:
        print("Let's go to the beach! 🏖️")
    else:
        print("Let's watch a movie at home. 🎬")
else:
    print("Time to work! 💼")


# ==============================================================================
# 2. FOR LOOPS
# ==============================================================================

print("\n2. FOR LOOPS")
print("-" * 30)

# Iterating over a list
fruits = ["Apple", "Banana", "Cherry"]
print("Fruits list:")
for fruit in fruits:
    print(f"  - {fruit}")

# Using range()
print("\nUsing range(5):")
for i in range(5):
    print(f"  Iteration {i}")

print("\nUsing range(2, 6): start at 2, stop before 6")
for i in range(2, 6):
    print(i, end=" ")
print()  # Newline

print("\nUsing range(0, 10, 2): start at 0, stop before 10, step 2")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Iterating over a string
word = "Python"
print(f"\nIterating over string '{word}':")
for char in word:
    print(char, end="-")
print()


# ==============================================================================
# 3. WHILE LOOPS
# ==============================================================================

print("\n3. WHILE LOOPS")
print("-" * 30)

# Basic while loop
count = 5
print("Countdown:")
while count > 0:
    print(count)
    count -= 1  # Important: decrement to avoid infinite loop!
print("Blastoff! 🚀")

# User input validation simulation
attempts = 0
max_attempts = 3
password = "secret"
input_password = ""

print("\nWhile loop with break simulation:")
# In a real app, you'd use input(). Here we simulate attempts.
simulated_inputs = ["wrong", "1234", "secret"]

for attempt_input in simulated_inputs:
    attempts += 1
    print(f"Attempt {attempts}: input '{attempt_input}'")
    if attempt_input == password:
        print("Access Granted! 🔓")
        break
    else:
        print("Access Denied 🔒")
else:
    # This block executes if the loop completes normally (without break)
    print("Max attempts reached.")


# ==============================================================================
# 4. LOOP CONTROL STATEMENTS (break, continue)
# ==============================================================================

print("\n4. LOOP CONTROL STATEMENTS")
print("-" * 30)

# break statement
print("Break example (stop at 5):")
for num in range(1, 11):
    if num == 5:
        print("Breaking the loop!")
        break
    print(num, end=" ")
print()

# continue statement
print("\nContinue example (skip even numbers):")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip the rest of the loop body for this iteration
    print(num, end=" ")
print()

# ==============================================================================
# 5. PRACTICAL EXAMPLES
# ==============================================================================

print("\n5. PRACTICAL EXAMPLES")
print("-" * 30)

# Example: Sum of numbers
numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total += n
print(f"Sum of {numbers} is {total}")

# Example: Finding max value without max()
max_val = numbers[0]
for n in numbers:
    if n > max_val:
        max_val = n
print(f"Max value is {max_val}")

print("\n" + "=" * 50)
print("🚀 End of Module 02 Demonstration")
