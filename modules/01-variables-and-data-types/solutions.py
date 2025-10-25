"""
Module 01: Variables and Data Types - Solutions

These are the solutions for the exercises in this module.
Try to solve the exercises yourself before looking here!
"""

# ==============================================================================
# EXERCISE 1: Variable Creation and Basic Types
# ==============================================================================

def exercise_1():
    """
    Create variables to store information about a book:
    - title (string)
    - author (string) 
    - publication_year (integer)
    - price (float)
    - is_available (boolean)
    
    Print all variables with descriptive labels.
    """
    title = "Python Crash Course"
    author = "Eric Matthes"
    publication_year = 2019
    price = 29.99
    is_available = True
    
    print("Book Information:")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Publication Year: {publication_year}")
    print(f"Price: ${price:.2f}")
    print(f"Available: {is_available}")

# ==============================================================================
# EXERCISE 2: Type Conversion Practice
# ==============================================================================

def exercise_2():
    """
    Perform the following type conversions:
    1. Convert string "123" to integer
    2. Convert float 45.67 to string
    3. Convert integer 100 to float
    4. Convert boolean True to integer
    5. Convert string "3.14" to float
    
    Print the original values and converted values.
    """
    # 1. String to integer
    str_num = "123"
    int_num = int(str_num)
    print(f"String '{str_num}' -> Integer {int_num}")
    
    # 2. Float to string
    float_num = 45.67
    str_float = str(float_num)
    print(f"Float {float_num} -> String '{str_float}'")
    
    # 3. Integer to float
    int_val = 100
    float_val = float(int_val)
    print(f"Integer {int_val} -> Float {float_val}")
    
    # 4. Boolean to integer
    bool_val = True
    int_bool = int(bool_val)
    print(f"Boolean {bool_val} -> Integer {int_bool}")
    
    # 5. String to float
    str_pi = "3.14"
    float_pi = float(str_pi)
    print(f"String '{str_pi}' -> Float {float_pi}")

# ==============================================================================
# EXERCISE 3: String Manipulation
# ==============================================================================

def exercise_3():
    """
    Given the string: "  Python Programming is FUN!  "
    1. Remove leading and trailing spaces
    2. Convert to lowercase
    3. Replace "fun" with "awesome"
    4. Extract the word "Programming"
    5. Check if the string starts with "Python"
    
    Print each result.
    """
    text = "  Python Programming is FUN!  "
    
    # 1. Remove spaces
    stripped = text.strip()
    print(f"1. Stripped: '{stripped}'")
    
    # 2. Convert to lowercase
    lower = stripped.lower()
    print(f"2. Lowercase: '{lower}'")
    
    # 3. Replace "fun" with "awesome"
    replaced = lower.replace("fun", "awesome")
    print(f"3. Replaced: '{replaced}'")
    
    # 4. Extract "Programming"
    # Find position and extract
    start = stripped.find("Programming")
    end = start + len("Programming")
    programming = stripped[start:end]
    print(f"4. Extracted: '{programming}'")
    
    # 5. Check if starts with "Python"
    starts_with_python = stripped.startswith("Python")
    print(f"5. Starts with 'Python': {starts_with_python}")

# ==============================================================================
# EXERCISE 4: Arithmetic Operations
# ==============================================================================

def exercise_4():
    """
    Calculate and print:
    1. The area of a rectangle (width=8.5, height=12.2)
    2. The average of numbers: 85, 90, 78, 92
    3. 2 raised to the power of 8
    4. The remainder when 27 is divided by 4
    5. The result of: (15 + 3 * 2) / 4
    
    Use variables for all calculations.
    """
    # 1. Rectangle area
    width = 8.5
    height = 12.2
    area = width * height
    print(f"1. Rectangle area: {width} * {height} = {area:.2f}")
    
    # 2. Average of numbers
    numbers = [85, 90, 78, 92]
    average = sum(numbers) / len(numbers)
    print(f"2. Average of {numbers}: {average:.2f}")
    
    # 3. Power
    power = 2 ** 8
    print(f"3. 2^8 = {power}")
    
    # 4. Remainder
    remainder = 27 % 4
    print(f"4. 27 % 4 = {remainder}")
    
    # 5. Expression
    result = (15 + 3 * 2) / 4
    print(f"5. (15 + 3 * 2) / 4 = {result}")

# ==============================================================================
# EXERCISE 5: String Formatting
# ==============================================================================

def exercise_5():
    """
    Create a formatted string that includes:
    - Your name
    - Your age
    - Your favorite programming language
    - The year you started learning Python
    
    Use f-strings to create a nice introduction message.
    """
    name = "Alex"
    age = 28
    language = "Python"
    start_year = 2024
    
    message = f"""
    Hello! My name is {name}.
    I'm {age} years old and my favorite programming language is {language}.
    I started learning {language} in {start_year}.
    """
    
    print(message)

# ==============================================================================
# EXERCISE 6: Boolean Logic
# ==============================================================================

def exercise_6():
    """
    Create variables for:
    - age (integer)
    - has_license (boolean)
    - has_car (boolean)
    
    Determine and print if a person can:
    - Drive (has license and age >= 16)
    - Rent a car (has license and age >= 25)
    - Get senior discount (age >= 65)
    """
    age = 22
    has_license = True
    has_car = False
    
    can_drive = has_license and age >= 16
    can_rent_car = has_license and age >= 25
    senior_discount = age >= 65
    
    print(f"Age: {age}")
    print(f"Has license: {has_license}")
    print(f"Has car: {has_car}")
    print(f"Can drive: {can_drive}")
    print(f"Can rent a car: {can_rent_car}")
    print(f"Gets senior discount: {senior_discount}")

# ==============================================================================
# EXERCISE 7: Multiple Assignment
# ==============================================================================

def exercise_7():
    """
    Use multiple assignment to:
    1. Assign three variables in one line: a=10, b=20, c=30
    2. Swap the values of two variables without a temporary variable
    3. Unpack a tuple (name, age, city) into separate variables
    
    Print all variables before and after operations.
    """
    # 1. Multiple assignment
    a, b, c = 10, 20, 30
    print(f"1. Multiple assignment: a={a}, b={b}, c={c}")
    
    # 2. Swap variables
    print(f"Before swap: x={a}, y={b}")
    a, b = b, a
    print(f"After swap: x={a}, y={b}")
    
    # 3. Unpack tuple
    person_info = ("Alice", 25, "New York")
    name, age, city = person_info
    print(f"3. Unpacked: name='{name}', age={age}, city='{city}'")

# ==============================================================================
# EXERCISE 8: Number Formatting
# ==============================================================================

def exercise_8():
    """
    Format the following numbers:
    1. 1234.5678 to 2 decimal places
    2. 0.4567 as a percentage with 1 decimal
    3. 1000000 with comma separators
    4. 3.1415926535 to 4 decimal places
    
    Print the original and formatted numbers.
    """
    num1 = 1234.5678
    num2 = 0.4567
    num3 = 1000000
    num4 = 3.1415926535
    
    print(f"1. {num1} -> {num1:.2f}")
    print(f"2. {num2} -> {num2:.1%}")
    print(f"3. {num3} -> {num3:,}")
    print(f"4. {num4} -> {num4:.4f}")

# ==============================================================================
# EXERCISE 9: String Methods
# ==============================================================================

def exercise_9():
    """
    Given the string: "Hello World of Python Programming"
    1. Convert to title case
    2. Count how many 'o' characters are in the string
    3. Find the position of "Python"
    4. Split the string into words
    5. Join the words with hyphens instead of spaces
    
    Print each result.
    """
    text = "Hello World of Python Programming"
    
    # 1. Title case
    title = text.title()
    print(f"1. Title case: '{title}'")
    
    # 2. Count 'o'
    count_o = text.count('o')
    print(f"2. Count of 'o': {count_o}")
    
    # 3. Find "Python"
    python_pos = text.find("Python")
    print(f"3. Position of 'Python': {python_pos}")
    
    # 4. Split into words
    words = text.split()
    print(f"4. Split: {words}")
    
    # 5. Join with hyphens
    hyphenated = "-".join(words)
    print(f"5. Hyphenated: '{hyphenated}'")

# ==============================================================================
# EXERCISE 10: Practical Application - Shopping Cart
# ==============================================================================

def exercise_10():
    """
    Create a shopping cart with 3 items. For each item store:
    - name (string)
    - quantity (integer) 
    - price (float)
    
    Calculate:
    - Total cost for each item (quantity * price)
    - Subtotal (sum of all item totals)
    - Tax (8.5% of subtotal)
    - Final total (subtotal + tax)
    
    Print a formatted receipt.
    """
    # Item 1
    item1_name = "Python Book"
    item1_quantity = 2
    item1_price = 29.99
    item1_total = item1_quantity * item1_price
    
    # Item 2
    item2_name = "Coffee Mug"
    item2_quantity = 1
    item2_price = 15.50
    item2_total = item2_quantity * item2_price
    
    # Item 3
    item3_name = "Stickers"
    item3_quantity = 5
    item3_price = 2.99
    item3_total = item3_quantity * item3_price
    
    # Calculations
    subtotal = item1_total + item2_total + item3_total
    tax_rate = 0.085
    tax = subtotal * tax_rate
    final_total = subtotal + tax
    
    # Print receipt
    print("🛒 SHOPPING RECEIPT")
    print("=" * 40)
    print(f"{item1_name:<15} {item1_quantity:>2} x ${item1_price:>6.2f} = ${item1_total:>7.2f}")
    print(f"{item2_name:<15} {item2_quantity:>2} x ${item2_price:>6.2f} = ${item2_total:>7.2f}")
    print(f"{item3_name:<15} {item3_quantity:>2} x ${item3_price:>6.2f} = ${item3_total:>7.2f}")
    print("-" * 40)
    print(f"Subtotal: ${subtotal:>26.2f}")
    print(f"Tax (8.5%): ${tax:>24.2f}")
    print("=" * 40)
    print(f"TOTAL: ${final_total:>28.2f}")

# ==============================================================================
# EXERCISE 11: Type Checking
# ==============================================================================

def exercise_11():
    """
    Create a list with different data types:
    [10, 3.14, "Hello", True, None, [1, 2, 3]]
    
    For each item in the list:
    - Print the value and its type
    - Check if it's a specific type using isinstance()
    
    Print your findings.
    """
    items = [10, 3.14, "Hello", True, None, [1, 2, 3]]
    
    for item in items:
        print(f"Value: {item!r:>10} | Type: {type(item).__name__:>8}", end=" | ")
        
        # Type checks
        checks = []
        if isinstance(item, int):
            checks.append("int")
        if isinstance(item, float):
            checks.append("float")
        if isinstance(item, str):
            checks.append("str")
        if isinstance(item, bool):
            checks.append("bool")
        if isinstance(item, type(None)):
            checks.append("None")
        if isinstance(item, list):
            checks.append("list")
            
        print(f"Is: {', '.join(checks)}")

# ==============================================================================
# EXERCISE 12: Compound Assignment
# ==============================================================================

def exercise_12():
    """
    Start with a variable x = 100
    Apply these operations in sequence:
    1. Add 25
    2. Multiply by 2
    3. Subtract 50
    4. Divide by 5
    5. Raise to power of 2
    
    Use compound assignment operators for each step.
    Print the value after each operation.
    """
    x = 100
    print(f"Initial: x = {x}")
    
    x += 25
    print(f"After x += 25: x = {x}")
    
    x *= 2
    print(f"After x *= 2: x = {x}")
    
    x -= 50
    print(f"After x -= 50: x = {x}")
    
    x /= 5
    print(f"After x /= 5: x = {x}")
    
    x **= 2
    print(f"After x **= 2: x = {x}")

# ==============================================================================
# EXERCISE 13: String Indexing and Slicing
# ==============================================================================

def exercise_13():
    """
    Given the string: "PythonProgramming"
    1. Extract first 6 characters
    2. Extract last 11 characters  
    3. Get every second character
    4. Reverse the string
    5. Extract "Program" from the string
    
    Print each result.
    """
    text = "PythonProgramming"
    
    # 1. First 6 characters
    first_6 = text[:6]
    print(f"1. First 6: '{first_6}'")
    
    # 2. Last 11 characters
    last_11 = text[-11:]
    print(f"2. Last 11: '{last_11}'")
    
    # 3. Every second character
    every_second = text[::2]
    print(f"3. Every second: '{every_second}'")
    
    # 4. Reverse
    reversed_text = text[::-1]
    print(f"4. Reversed: '{reversed_text}'")
    
    # 5. Extract "Program"
    # "Program" starts at index 6 and is 7 characters long
    program = text[6:13]
    print(f"5. 'Program': '{program}'")

# ==============================================================================
# EXERCISE 14: Temperature Converter Function
# ==============================================================================

def exercise_14():
    """
    Create a temperature converter that:
    - Converts Celsius to Fahrenheit: F = (C × 9/5) + 32
    - Converts Fahrenheit to Celsius: C = (F - 32) × 5/9
    
    Test with:
    - 0°C to Fahrenheit
    - 100°C to Fahrenheit  
    - 32°F to Celsius
    - 212°F to Celsius
    
    Print all conversions with clear labels.
    """
    # Celsius to Fahrenheit
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    # Fahrenheit to Celsius
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    
    # Test conversions
    tests = [
        (0, "C", "F"),
        (100, "C", "F"),
        (32, "F", "C"),
        (212, "F", "C")
    ]
    
    for temp, from_unit, to_unit in tests:
        if from_unit == "C":
            converted = celsius_to_fahrenheit(temp)
        else:
            converted = fahrenheit_to_celsius(temp)
        
        print(f"{temp}°{from_unit} = {converted:.2f}°{to_unit}")

# ==============================================================================
# EXERCISE 15: User Profile Formatter
# ==============================================================================

def exercise_15():
    """
    Create a user profile with:
    - username
    - full_name
    - age
    - email
    - is_premium_member
    
    Format and print the profile in two different ways:
    1. Using f-strings with alignment
    2. Using str.format() method
    
    Make the output look like a proper user profile card.
    """
    username = "python_dev"
    full_name = "Alex Johnson"
    age = 28
    email = "alex.johnson@email.com"
    is_premium_member = True
    
    print("Method 1: f-strings")
    print("=" * 30)
    print(f"""
    ┌────────────────────────────┐
    │        USER PROFILE        │
    ├────────────────────────────┤
    │ Username:    {username:<15} │
    │ Full Name:   {full_name:<15} │
    │ Age:         {age:<15} │
    │ Email:       {email:<15} │
    │ Premium:     {is_premium_member!s:<15} │
    └────────────────────────────┘
    """)
    
    print("Method 2: str.format()")
    print("=" * 30)
    profile_template = """
    ┌────────────────────────────┐
    │        USER PROFILE        │
    ├────────────────────────────┤
    │ Username:    {username:<15} │
    │ Full Name:   {full_name:<15} │
    │ Age:         {age:<15} │
    │ Email:       {email:<15} │
    │ Premium:     {premium:<15} │
    └────────────────────────────┘
    """
    print(profile_template.format(
        username=username,
        full_name=full_name,
        age=age,
        email=email,
        premium=str(is_premium_member)
    ))

# ==============================================================================
# MAIN FUNCTION TO RUN ALL SOLUTIONS
# ==============================================================================

def main():
    """
    Run all exercise solutions in sequence.
    """
    print("Module 01: Variables and Data Types - Solutions")
    print("=" * 50)
    
    exercises = [
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
        exercise_6, exercise_7, exercise_8, exercise_9, exercise_10,
        exercise_11, exercise_12, exercise_13, exercise_14, exercise_15
    ]
    
    for i, exercise in enumerate(exercises, 1):
        print(f"\nExercise {i}:")
        print("-" * 12)
        exercise()

if __name__ == "__main__":
    main()