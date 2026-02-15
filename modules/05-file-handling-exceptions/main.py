"""
Module 05: File Handling and Exceptions

This module covers:
- Reading from and writing to files
- Working with different file modes
- Context managers (with statement)
- Exception handling with try/except/finally
- Creating custom exceptions
"""

import os
import json

print("📁 Module 05: File Handling and Exceptions")
print("=" * 50)

# ==============================================================================
# 1. BASIC FILE OPERATIONS
# ==============================================================================

print("\n1. BASIC FILE OPERATIONS")
print("-" * 30)

# Writing to a file
print("Writing to file 'sample.txt'...")
with open('sample.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling is easy!\n")
print("✅ File written successfully")

# Reading from a file
print("\nReading from file 'sample.txt':")
with open('sample.txt', 'r') as file:
    content = file.read()
    print(f"Content:\n{content}")

# Reading line by line
print("\nReading line by line:")
with open('sample.txt', 'r') as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Appending to a file
print("\nAppending to file...")
with open('sample.txt', 'a') as file:
    file.write("This line was appended!\n")
print("✅ Content appended")

# Reading all lines into a list
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    print(f"\nAll lines as list: {lines}")

# ==============================================================================
# 2. FILE MODES
# ==============================================================================

print("\n2. FILE MODES")
print("-" * 30)

print("""
Common file modes:
'r'  - Read (default)
'w'  - Write (creates new file or truncates existing)
'a'  - Append (writes to end of file)
'x'  - Exclusive creation (fails if file exists)
'b'  - Binary mode (e.g., 'rb', 'wb')
't'  - Text mode (default)
'r+' - Read and write
'w+' - Write and read (truncates file)
'a+' - Append and read
""")

# Binary file example
print("\nWriting binary data:")
with open('binary.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')
print("✅ Binary file written")

with open('binary.bin', 'rb') as file:
    binary_data = file.read()
    print(f"Binary data read: {binary_data}")

# Clean up
os.remove('binary.bin')

# ==============================================================================
# 3. WORKING WITH DIFFERENT FILE TYPES
# ==============================================================================

print("\n3. WORKING WITH DIFFERENT FILE TYPES")
print("-" * 30)

# JSON files
print("\nJSON file example:")
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding", "hiking"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

# Write JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)
print("✅ JSON file written")

# Read JSON
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(f"JSON data read: {loaded_data}")

# CSV-like file (comma-separated)
print("\nCSV-like file example:")
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"],
    ["Charlie", "35", "Chicago"]
]

with open('data.csv', 'w') as file:
    for row in csv_data:
        file.write(','.join(row) + '\n')
print("✅ CSV file written")

with open('data.csv', 'r') as file:
    for line in file:
        print(f"  {line.strip()}")

# ==============================================================================
# 4. EXCEPTION HANDLING BASICS
# ==============================================================================

print("\n4. EXCEPTION HANDLING BASICS")
print("-"*30)

# Basic try-except
print("\nBasic try-except:")
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("❌ That's not a valid number!")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

# try-except-else-finally
print("\nTry-except-else-finally:")
try:
    file = open('nonexistent.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("❌ File not found!")
else:
    print(f"✅ File content: {content}")
    file.close()
finally:
    print("✅ This always executes!")

# Multiple exceptions in one except block
print("\nHandling multiple exceptions:")
try:
    numbers = [1, 2, 3]
    index = int(input("Enter index (0-2): "))
    print(f"Value at index {index}: {numbers[index]}")
except (ValueError, IndexError) as e:
    print(f"❌ Error: {e}")

# ==============================================================================
# 5. COMMON EXCEPTIONS
# ==============================================================================

print("\n5. COMMON EXCEPTIONS")
print("-" * 30)

# Demonstrate various exceptions
exceptions_demo = [
    ("FileNotFoundError", lambda: open('nonexistent.txt')),
    ("ZeroDivisionError", lambda: 1/0),
    ("ValueError", lambda: int("abc")),
    ("TypeError", lambda: "hello" + 5),
    ("IndexError", lambda: [1,2,3][10]),
    ("KeyError", lambda: {"a":1}['b']),
    ("AttributeError", lambda: "hello".nonexistent_method()),
]

for name, func in exceptions_demo:
    try:
        func()
    except Exception as e:
        print(f"  {name}: {e}")

# ==============================================================================
# 6. RAISING EXCEPTIONS
# ==============================================================================

print("\n6. RAISING EXCEPTIONS")
print("-" * 30)

def validate_age(age):
    """Validate age with custom error messages."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems too high")
    return True

# Test the validation
test_ages = [25, -5, 200, "twenty"]
for age in test_ages:
    try:
        validate_age(age)
        print(f"  Age {age}: ✅ Valid")
    except (TypeError, ValueError) as e:
        print(f"  Age {age}: ❌ {e}")

# ==============================================================================
# 7. CUSTOM EXCEPTIONS
# ==============================================================================

print("\n7. CUSTOM EXCEPTIONS")
print("-" * 30)

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds: balance ${balance}, tried to withdraw ${amount}"
        super().__init__(self.message)

class NegativeAmountError(Exception):
    """Raised when negative amount is provided."""
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot deposit negative amount")
        self.balance += amount
        print(f"  Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"  Withdrew ${amount}. New balance: ${self.balance}")

# Test custom exceptions
print("\nTesting BankAccount with custom exceptions:")
account = BankAccount("Alice", 100)

try:
    account.withdraw(150)  # Should raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"  ❌ {e}")

try:
    account.deposit(-50)  # Should raise NegativeAmountError
except NegativeAmountError as e:
    print(f"  ❌ {e}")

# Valid operations
try:
    account.deposit(50)
    account.withdraw(30)
except (InsufficientFundsError, NegativeAmountError) as e:
    print(f"  ❌ {e}")

# ==============================================================================
# 8. CONTEXT MANAGERS (WITH STATEMENT)
# ==============================================================================

print("\n8. CONTEXT MANAGERS")
print("-" * 30)

# Custom context manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"  Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions, True to suppress them
        return False

# Use custom context manager
print("\nUsing custom context manager:")
with FileManager('test.txt', 'w') as f:
    f.write("Hello from custom context manager!")

with FileManager('test.txt', 'r') as f:
    content = f.read()
    print(f"  Read content: {content}")

# Clean up
os.remove('test.txt')

# ==============================================================================
# 9. PRACTICAL EXAMPLES
# ==============================================================================

print("\n9. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Safe file reader
def safe_read_file(filename):
    """Safely read a file with proper error handling."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"  File '{filename}' not found")
        return None
    except PermissionError:
        print(f"  Permission denied to read '{filename}'")
        return None
    except Exception as e:
        print(f"  Error reading file: {e}")
        return None

print("\nSafe file reader example:")
content = safe_read_file('existing.txt')  # Doesn't exist
content = safe_read_file('sample.txt')    # Exists
if content:
    print(f"  File content: {content[:50]}...")

# Example 2: Data processing with validation
def process_user_data(data):
    """Process user data with validation."""
    required_fields = ['name', 'email', 'age']
    
    # Check for missing fields
    for field in required_fields:
        if field not in data:
            raise KeyError(f"Missing required field: {field}")
    
    # Validate age
    try:
        age = int(data['age'])
        if age < 0 or age > 150:
            raise ValueError(f"Invalid age: {age}")
    except ValueError:
        raise ValueError("Age must be a valid number")
    
    # Validate email
    if '@' not in data['email']:
        raise ValueError("Invalid email format")
    
    return {
        'name': data['name'].strip(),
        'email': data['email'].lower(),
        'age': age
    }

print("\nData processing example:")
test_data = [
    {'name': 'Alice', 'email': 'alice@example.com', 'age': '25'},
    {'name': 'Bob', 'email': 'bob.com', 'age': '30'},
    {'name': 'Charlie', 'email': 'charlie@example.com', 'age': '200'},
    {'name': 'Diana', 'age': '28'},  # Missing email
]

for data in test_data:
    try:
        processed = process_user_data(data)
        print(f"  ✅ Processed: {processed}")
    except (KeyError, ValueError) as e:
        print(f"  ❌ Error: {e}")

# Example 3: Logging exceptions
import logging
import traceback

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide_with_logging(a, b):
    """Divide with exception logging."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        logging.error(f"Division by zero: {a}/{b}")
        print("  ❌ Cannot divide by zero")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}\n{traceback.format_exc()}")
        print(f"  ❌ Error: {e}")
        return None

print("\nException logging example:")
print(f"  10/2 = {divide_with_logging(10, 2)}")
print(f"  10/0 = {divide_with_logging(10, 0)}")

# ==============================================================================
# 10. BEST PRACTICES
# ==============================================================================

print("\n10. BEST PRACTICES")
print("-" * 30)

print("""
✅ DO:
• Use specific exceptions rather than bare 'except:'
• Use context managers (with statement) for file operations
• Clean up resources in finally blocks
• Log exceptions for debugging
• Create custom exceptions for domain-specific errors

❌ DON'T:
• Catch exceptions you can't handle
• Use bare except: statements
• Ignore exceptions (pass without handling)
• Raise generic Exception
• Let exceptions propagate without handling at appropriate level
""")

# Example of good practice
def good_practice_example(filename):
    """Example following best practices."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Process data
        result = data.get('value', 0) * 2
        
    except FileNotFoundError:
        print(f"  File {filename} not found - using default")
        result = 0
    except json.JSONDecodeError:
        print(f"  Invalid JSON in {filename}")
        result = 0
    except Exception as e:
        print(f"  Unexpected error: {e}")
        logging.error(f"Error in good_practice_example: {e}")
        result = 0
    else:
        print(f"  Successfully processed {filename}")
    finally:
        print(f"  Finished processing {filename}")
    
    return result

# ==============================================================================
# CLEANUP
# ==============================================================================

print("\n" + "=" * 50)
print("CLEANING UP EXAMPLE FILES")
print("-" * 30)

# Remove example files
files_to_remove = ['sample.txt', 'data.json', 'data.csv', 'app.log']
for file in files_to_remove:
    try:
        if os.path.exists(file):
            os.remove(file)
            print(f"  Removed {file}")
    except Exception as e:
        print(f"  Error removing {file}: {e}")

# ==============================================================================
# NEXT STEPS
# ==============================================================================

print("\n" + "=" * 50)
print("NEXT STEPS")
print("=" * 50)

print("""
Great job learning about file handling and exceptions! 🎉

Next, you should:
1. Complete the exercises in exercises.py
2. Check your solutions with solutions.py
3. Take the quiz in quiz.py
4. Review the cheat-sheet.md for quick reference
5. Move on to Module 06: Object-Oriented Programming (OOP)

Key takeaways from this module:
• Always use context managers (with) for file operations
• Handle specific exceptions, not generic ones
• Use try/except/else/finally for robust error handling
• Create custom exceptions for domain-specific errors
• Log exceptions for debugging and monitoring
• Always clean up resources (files, network connections)

Remember: Good error handling makes your applications robust and user-friendly!
""")

print("🚀 You're becoming a more proficient Python programmer!")