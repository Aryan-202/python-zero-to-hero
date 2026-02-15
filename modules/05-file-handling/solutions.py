"""
Module 05: File Handling & Exceptions - Solutions
"""

print("--- Module 05 Solutions ---")

# ==============================================================================
# Exercise 1: Write to File
# ==============================================================================
print("\nExercise 1: Write to File")

def write_shopping_list(items):
    try:
        with open("shopping_list.txt", "w") as f:
            for item in items:
                f.write(item + "\n")
        print("Successfully wrote items to shopping_list.txt")
    except IOError as e:
        print(f"Error writing file: {e}")

items = ["Apples", "Bananas", "Milk", "Bread"]
write_shopping_list(items)


# ==============================================================================
# Exercise 2: Read and Count
# ==============================================================================
print("\nExercise 2: Read and Count")

def count_lines(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

print(f"Items in list: {count_lines('shopping_list.txt')}")
print(f"Items in missing file: {count_lines('missing.txt')}")


# ==============================================================================
# Exercise 3: Safe Division
# ==============================================================================
print("\nExercise 3: Safe Division")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Inputs must be numbers.")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"5 / 0 = {safe_divide(5, 0)}")
print(f"string / 2 = {safe_divide('a', 2)}")
