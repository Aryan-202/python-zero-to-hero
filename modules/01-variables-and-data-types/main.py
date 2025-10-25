"""
Module 01: Variables and Data Types

This module covers the fundamental building blocks of Python programming:
variables, data types, type conversion, and basic operations.
"""

print("📊 Module 01: Variables and Data Types")
print("=" * 50)

# ==============================================================================
# 1. BASIC DATA TYPES IN PYTHON
# ==============================================================================

print("\n1. BASIC DATA TYPES IN PYTHON")
print("-" * 30)

# Integer (whole numbers)
age = 25
year = 2024
temperature = -5

print("Integers (int):")
print(f"  age = {age} (type: {type(age)})")
print(f"  year = {year} (type: {type(year)})")
print(f"  temperature = {temperature} (type: {type(temperature)})")

# Float (decimal numbers)
height = 5.9
weight = 68.5
pi = 3.14159

print("\nFloats (float):")
print(f"  height = {height} (type: {type(height)})")
print(f"  weight = {weight} (type: {type(weight)})")
print(f"  pi = {pi} (type: {type(pi)})")

# String (text)
name = "Alice"
message = 'Hello, World!'
multiline_string = """This is a
multi-line
string"""

print("\nStrings (str):")
print(f"  name = {name} (type: {type(name)})")
print(f"  message = {message} (type: {type(message)})")
print(f"  multiline_string = {multiline_string}")

# Boolean (True/False)
is_student = True
has_license = False
is_sunny = True

print("\nBooleans (bool):")
print(f"  is_student = {is_student} (type: {type(is_student)})")
print(f"  has_license = {has_license} (type: {type(has_license)})")
print(f"  is_sunny = {is_sunny} (type: {type(is_sunny)})")

# ==============================================================================
# 2. VARIABLE NAMING AND ASSIGNMENT
# ==============================================================================

print("\n2. VARIABLE NAMING AND ASSIGNMENT")
print("-" * 35)

# Valid variable names
first_name = "John"
last_name = "Doe"
age2 = 30
_private_var = "private"
MAX_SIZE = 100  # Constants are often in uppercase

print("Valid variable names:")
print(f"  first_name = {first_name}")
print(f"  last_name = {last_name}")
print(f"  age2 = {age2}")
print(f"  _private_var = {_private_var}")
print(f"  MAX_SIZE = {MAX_SIZE}")

# Multiple assignment
x, y, z = 10, 20, 30
name, age, city = "Bob", 25, "New York"

print("\nMultiple assignment:")
print(f"  x, y, z = {x}, {y}, {z}")
print(f"  name, age, city = {name}, {age}, {city}")

# Swapping variables
a = 5
b = 10
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a  # Pythonic way to swap
print(f"After swap: a = {a}, b = {b}")

# ==============================================================================
# 3. TYPE CONVERSION
# ==============================================================================

print("\n3. TYPE CONVERSION")
print("-" * 20)

# Converting between types
number_str = "123"
number_int = int(number_str)
number_float = float(number_str)

print(f"Original string: '{number_str}' (type: {type(number_str)})")
print(f"Converted to int: {number_int} (type: {type(number_int)})")
print(f"Converted to float: {number_float} (type: {type(number_float)})")

# More conversions
float_num = 45.7
int_num = int(float_num)  # Truncates decimal part
str_num = str(float_num)
bool_val = bool(float_num)

print(f"\nFloat: {float_num}")
print(f"Converted to int: {int_num} (loses decimal)")
print(f"Converted to str: '{str_num}'")
print(f"Converted to bool: {bool_val}")

# Boolean conversion examples
print("\nBoolean conversion examples:")
print(f"  bool(0) = {bool(0)}")
print(f"  bool(1) = {bool(1)}")
print(f"  bool('') = {bool('')}")
print(f"  bool('Hello') = {bool('Hello')}")
print(f"  bool([]) = {bool([])}")
print(f"  bool([1, 2, 3]) = {bool([1, 2, 3])}")

# ==============================================================================
# 4. STRING OPERATIONS AND METHODS
# ==============================================================================

print("\n4. STRING OPERATIONS AND METHODS")
print("-" * 35)

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Concatenation: {first_name} + ' ' + {last_name} = {full_name}")

# String repetition
hello = "Hello! "
repeated_hello = hello * 3
print(f"Repetition: '{hello}' * 3 = '{repeated_hello}'")

# String methods
text = "  hello World!  "
print(f"\nOriginal text: '{text}'")
print(f"Upper case: '{text.upper()}'")
print(f"Lower case: '{text.lower()}'")
print(f"Title case: '{text.title()}'")
print(f"Strip spaces: '{text.strip()}'")
print(f"Replace 'World' with 'Python': '{text.replace('World', 'Python')}'")
print(f"Starts with 'hello': {text.strip().startswith('hello')}")
print(f"Ends with '!': {text.strip().endswith('!')}")

# String indexing and slicing
message = "Python Programming"
print(f"\nString: '{message}'")
print(f"First character: '{message[0]}'")
print(f"Last character: '{message[-1]}'")
print(f"Characters 0-5: '{message[0:6]}'")
print(f"Every second character: '{message[::2]}'")
print(f"Reverse: '{message[::-1]}'")

# String length
print(f"Length of string: {len(message)} characters")

# ==============================================================================
# 5. NUMERIC OPERATIONS
# ==============================================================================

print("\n5. NUMERIC OPERATIONS")
print("-" * 25)

# Basic arithmetic
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")

# Compound assignment operators
x = 10
print(f"\nInitial x = {x}")
x += 5  # x = x + 5
print(f"After x += 5: {x}")
x -= 3  # x = x - 3
print(f"After x -= 3: {x}")
x *= 2  # x = x * 2
print(f"After x *= 2: {x}")
x //= 4  # x = x // 4
print(f"After x //= 4: {x}")

# Comparison operators
num1 = 10
num2 = 20

print(f"\nComparison: {num1} vs {num2}")
print(f"  {num1} == {num2}: {num1 == num2}")
print(f"  {num1} != {num2}: {num1 != num2}")
print(f"  {num1} < {num2}: {num1 < num2}")
print(f"  {num1} > {num2}: {num1 > num2}")
print(f"  {num1} <= {num2}: {num1 <= num2}")
print(f"  {num1} >= {num2}: {num1 >= num2}")

# ==============================================================================
# 6. STRING FORMATTING
# ==============================================================================

print("\n6. STRING FORMATTING")
print("-" * 25)

# Old-style formatting (%)
name = "Alice"
age = 25
print("Old-style formatting:")
print("Hello, %s! You are %d years old." % (name, age))

# str.format() method
print("\nstr.format() method:")
print("Hello, {}! You are {} years old.".format(name, age))
print("Hello, {1}! You are {0} years old.".format(age, name))
print("Hello, {name}! You are {age} years old.".format(name=name, age=age))

# f-strings (Python 3.6+)
print("\nf-strings (recommended):")
print(f"Hello, {name}! You are {age} years old.")
print(f"Next year you'll be {age + 1} years old.")

# Formatting numbers
price = 19.999
percentage = 0.4567
print(f"\nNumber formatting:")
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Percentage: {percentage:.1%}")  # Percentage with 1 decimal
print(f"Large number: {1000000:,}")  # Comma separator

# ==============================================================================
# 7. BOOLEAN OPERATIONS
# ==============================================================================

print("\n7. BOOLEAN OPERATIONS")
print("-" * 25)

# Logical operators
has_license = True
has_car = False
age = 18

print(f"has_license = {has_license}, has_car = {has_car}, age = {age}")

# AND operator (both must be True)
can_drive = has_license and age >= 16
print(f"Can drive (has_license AND age >= 16): {can_drive}")

# OR operator (at least one True)
can_rent_car = has_license or has_car
print(f"Can rent car (has_license OR has_car): {can_rent_car}")

# NOT operator (inverts the value)
cannot_drive = not has_license
print(f"Cannot drive (NOT has_license): {cannot_drive}")

# Complex conditions
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday
print(f"Can sleep in (is_weekend OR is_holiday): {can_sleep_in}")

# ==============================================================================
# 8. PRACTICAL EXAMPLES
# ==============================================================================

print("\n8. PRACTICAL EXAMPLES")
print("-" * 25)

# Example 1: User profile
print("Example 1: User Profile")
username = "python_learner"
posts = 15
followers = 234
is_verified = True
join_date = "2024-01-15"

print(f"""
User Profile:
------------
Username: @{username}
Posts: {posts}
Followers: {followers:,}
Verified: {is_verified}
Join Date: {join_date}
""")

# Example 2: Shopping cart
print("Example 2: Shopping Cart")
item_name = "Python Programming Book"
quantity = 2
price_per_item = 29.99
total_cost = quantity * price_per_item

print(f"""
Shopping Cart:
-------------
Item: {item_name}
Quantity: {quantity}
Price per item: ${price_per_item:.2f}
Total: ${total_cost:.2f}
""")

# Example 3: Temperature converter
print("Example 3: Temperature Converter")
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit:.1f}°F")

# ==============================================================================
# 9. TYPE CHECKING AND IDENTITY
# ==============================================================================

print("\n9. TYPE CHECKING AND IDENTITY")
print("-" * 35)

# Using type() function
values = [42, 3.14, "Hello", True, None]

print("Type checking:")
for value in values:
    print(f"  Value: {value:>10} -> Type: {type(value).__name__:>8}")

# Using isinstance()
number = 100
print(f"\nisinstance() examples:")
print(f"  isinstance({number}, int): {isinstance(number, int)}")
print(f"  isinstance({number}, (int, float)): {isinstance(number, (int, float))}")

# Identity operator (is)
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"\nIdentity comparison:")
print(f"  x is z: {x is z}")  # True (same object)
print(f"  x is y: {x is y}")  # False (different objects with same value)
print(f"  x == y: {x == y}")  # True (same value)

# ==============================================================================
# NEXT STEPS
# ==============================================================================

print("\n" + "=" * 50)
print("NEXT STEPS")
print("=" * 50)

print("""
Great job learning about variables and data types! 🎉

Next, you should:
1. Complete the exercises in exercises.py
2. Check your solutions with solutions.py  
3. Take the quiz in quiz.py
4. Review the cheat-sheet.md for quick reference
5. Move on to Module 02: Control Structures

Key takeaways from this module:
• Python has several built-in data types (int, float, str, bool)
• Variables store data and can be reassigned
• Type conversion lets you change between data types
• Strings have many useful methods for manipulation
• Boolean logic helps make decisions in code

Remember to practice regularly and experiment with different data types!
""")

print("🚀 You're building a solid foundation in Python programming!")