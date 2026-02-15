"""
Module 05: File Handling & Exceptions
"""

print("📂 Module 05: File Handling & Exceptions")
print("=" * 50)

# Writing to a file
print("\n1. Writing to a file")
with open("example.txt", "w") as f:
    f.write("Hello from Python!\nThis is a file.\n")
print("File 'example.txt' written successfully.")

# Reading from a file
print("\n2. Reading from a file")
try:
    with open("example.txt", "r") as f:
        content = f.read()
        print("--- File Content ---")
        print(content)
        print("--------------------")
except FileNotFoundError:
    print("Error: The file does not exist!")

# Exception Handling
print("\n3. Exception Handling")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Caught an error: Cannot divide by zero! 🚫")
finally:
    print("This block runs no matter what.")
