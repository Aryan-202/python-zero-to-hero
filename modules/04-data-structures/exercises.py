"""
Module 04: Data Structures - Exercises

Practice working with lists, tuples, dictionaries, and sets.
Try to solve these exercises without looking at the solutions first!
"""

# ==============================================================================
# EXERCISE 1: List Operations
# ==============================================================================

def exercise_1():
    """
    Create a list called 'fruits' containing: "apple", "banana", "orange", "grape", "mango"
    
    Then perform the following operations:
    1. Print the entire list
    2. Print the first and last fruit
    3. Add "kiwi" to the end of the list
    4. Insert "strawberry" at index 2
    5. Remove "banana" from the list
    6. Sort the list alphabetically
    7. Print the length of the list
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 2: List Comprehension
# ==============================================================================

def exercise_2():
    """
    Use list comprehension to:
    1. Create a list of squares for numbers 1 through 10
    2. Create a list of even numbers from 1 to 20
    3. Create a list of uppercase versions of: ["hello", "world", "python"]
    4. Create a list of lengths for each word in: ["cat", "elephant", "dog", "butterfly"]
    
    Print each resulting list.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 3: Tuple Operations
# ==============================================================================

def exercise_3():
    """
    Create a tuple called 'coordinates' with values (10, 20, 30)
    
    Then:
    1. Print the tuple and its type
    2. Print the first and last element
    3. Try to modify the first element (this should fail - note the error)
    4. Create a new tuple by concatenating coordinates with (40, 50)
    5. Unpack the tuple into variables x, y, z and print them
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 4: Dictionary Basics
# ==============================================================================

def exercise_4():
    """
    Create a dictionary called 'student' with the following key-value pairs:
    - "name": "John Doe"
    - "age": 20
    - "grade": "A"
    - "subjects": ["Math", "Physics", "Computer Science"]
    
    Then:
    1. Print the student's name
    2. Add a new key "city" with value "New York"
    3. Update the age to 21
    4. Remove the "grade" key
    5. Print all keys, all values, and all key-value pairs
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 5: Dictionary Methods
# ==============================================================================

def exercise_5():
    """
    Given the dictionary:
    inventory = {"apples": 10, "bananas": 5, "oranges": 8, "grapes": 15}
    
    Perform the following:
    1. Check if "apples" exists in the inventory
    2. Get the value for "bananas" using the get() method
    3. Get the value for "pears" with a default of 0 using get()
    4. Print all items using the items() method
    5. Create a new dictionary with default values of 0 for ["mango", "kiwi", "peach"]
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 6: Set Operations
# ==============================================================================

def exercise_6():
    """
    Create two sets:
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    Calculate and print:
    1. Union of both sets
    2. Intersection of both sets
    3. Difference (set_a - set_b)
    4. Symmetric difference (elements in either set but not both)
    5. Check if set_a is a subset of set_b
    6. Add 9 to set_a
    7. Remove 1 from set_a
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 7: Nested Data Structures
# ==============================================================================

def exercise_7():
    """
    Create a nested data structure representing a school:
    
    school = {
        "name": "Python High School",
        "students": [
            {"name": "Alice", "grade": 9, "subjects": ["Math", "Science"]},
            {"name": "Bob", "grade": 10, "subjects": ["English", "History"]},
            {"name": "Charlie", "grade": 9, "subjects": ["Math", "Art"]}
        ],
        "teachers": ["Mr. Smith", "Ms. Johnson", "Dr. Brown"]
    }
    
    Then:
    1. Print the school name
    2. Print all student names
    3. Print Bob's subjects
    4. Add a new student: {"name": "Diana", "grade": 11, "subjects": ["Physics", "Chemistry"]}
    5. Print the total number of students
    6. Find all students in grade 9
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 8: List Manipulation Algorithms
# ==============================================================================

def exercise_8():
    """
    Implement the following functions WITHOUT using built-in methods
    like sum(), max(), min(), or sorted():
    
    1. calculate_sum(numbers) - returns the sum of all numbers
    2. find_max(numbers) - returns the largest number
    3. find_min(numbers) - returns the smallest number
    4. reverse_list(items) - returns a new list in reverse order
    5. count_occurrences(items, target) - returns how many times target appears
    
    Test your functions with: numbers = [3, 7, 2, 9, 1, 7, 4, 7]
    """
    # TODO: Write your functions here
    
    def calculate_sum(numbers):
        pass
    
    def find_max(numbers):
        pass
    
    def find_min(numbers):
        pass
    
    def reverse_list(items):
        pass
    
    def count_occurrences(items, target):
        pass
    
    # Test your functions
    numbers = [3, 7, 2, 9, 1, 7, 4, 7]
    # Call your functions here

# ==============================================================================
# EXERCISE 9: Dictionary Counting
# ==============================================================================

def exercise_9():
    """
    Given a string: "the quick brown fox jumps over the lazy dog"
    
    Use a dictionary to:
    1. Count the frequency of each letter (ignore spaces)
    2. Count the frequency of each word
    3. Find the most common letter
    4. Find the most common word
    
    Print the results.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 10: Set Operations for Data Analysis
# ==============================================================================

def exercise_10():
    """
    You have two lists of students:
    math_students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    science_students = ["Charlie", "David", "Frank", "Grace", "Henry"]
    
    Find:
    1. Students taking both math and science
    2. Students taking only math
    3. Students taking only science
    4. All unique students (union)
    5. Students taking exactly one subject (symmetric difference)
    
    Print all results.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 11: List Filtering and Transformation
# ==============================================================================

def exercise_11():
    """
    Given a list of mixed data types:
    mixed = [10, "hello", 3.14, True, "world", 42, False, "python", 2.5]
    
    Create three separate lists using list comprehension:
    1. strings_list - containing only strings
    2. numbers_list - containing only integers and floats
    3. booleans_list - containing only booleans
    
    Print each list.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 12: Dictionary of Lists
# ==============================================================================

def exercise_12():
    """
    Create a gradebook dictionary where:
    - Keys are student names
    - Values are lists of their grades
    
    grades = {
        "Alice": [85, 90, 78, 92],
        "Bob": [75, 82, 88, 79],
        "Charlie": [95, 89, 93, 97],
        "Diana": [70, 68, 75, 72]
    }
    
    Calculate and print:
    1. Each student's average grade
    2. The class average (average of all grades)
    3. The student with the highest average
    4. All students who have an average above 85
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 13: Matrix Operations with Lists
# ==============================================================================

def exercise_13():
    """
    Create a 3x3 matrix as a list of lists:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    Perform the following operations:
    1. Print the element at row 1, column 2 (remember 0-indexing)
    2. Print the entire first row
    3. Print the entire second column
    4. Calculate the sum of all elements
    5. Calculate the sum of the main diagonal (1, 5, 9)
    6. Transpose the matrix (rows become columns)
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 14: Shopping Cart with Dictionaries
# ==============================================================================

def exercise_14():
    """
    Implement a simple shopping cart using a dictionary where:
    - Keys are item names
    - Values are dictionaries with 'price' and 'quantity'
    
    cart = {}
    
    Implement these functions:
    1. add_item(cart, name, price, quantity) - adds item to cart
    2. remove_item(cart, name) - removes item from cart
    3. update_quantity(cart, name, quantity) - updates item quantity
    4. calculate_total(cart) - returns total cost
    5. display_cart(cart) - prints formatted cart contents
    
    Test your functions with sample data.
    """
    # TODO: Write your functions here
    
    def add_item(cart, name, price, quantity):
        pass
    
    def remove_item(cart, name):
        pass
    
    def update_quantity(cart, name, quantity):
        pass
    
    def calculate_total(cart):
        pass
    
    def display_cart(cart):
        pass
    
    # Test your functions
    cart = {}
    # Add test code here

# ==============================================================================
# EXERCISE 15: Data Structure Conversion
# ==============================================================================

def exercise_15():
    """
    Given the following data in different formats:
    
    # List of tuples (name, age, city)
    people_list = [("Alice", 25, "NYC"), ("Bob", 30, "LA"), ("Charlie", 35, "Chicago")]
    
    # Dictionary with names as keys and (age, city) as values
    people_dict = {"Alice": (25, "NYC"), "Bob": (30, "LA"), "Charlie": (35, "Chicago")}
    
    Perform the following conversions:
    1. Convert people_list to a dictionary similar to people_dict
    2. Convert people_dict to a list of tuples similar to people_list
    3. Create a set of all cities
    4. Create a list of all people older than 28
    5. Create a dictionary grouping people by city
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# MAIN FUNCTION TO RUN ALL EXERCISES
# ==============================================================================

def main():
    """
    Run all exercises in sequence.
    Uncomment the exercises you want to test.
    """
    print("Module 04: Data Structures - Exercises")
    print("=" * 50)
    
    # Uncomment the exercises you want to run:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()
    # exercise_11()
    # exercise_12()
    # exercise_13()
    # exercise_14()
    # exercise_15()

if __name__ == "__main__":
    main()