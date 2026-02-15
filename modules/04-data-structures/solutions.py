"""
Module 04: Data Structures - Solutions

These are the solutions for the exercises in this module.
Try to solve the exercises yourself before looking here!
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
    # Create the list
    fruits = ["apple", "banana", "orange", "grape", "mango"]
    
    # 1. Print entire list
    print(f"1. Original list: {fruits}")
    
    # 2. Print first and last
    print(f"2. First fruit: {fruits[0]}, Last fruit: {fruits[-1]}")
    
    # 3. Add "kiwi" to the end
    fruits.append("kiwi")
    print(f"3. After append: {fruits}")
    
    # 4. Insert "strawberry" at index 2
    fruits.insert(2, "strawberry")
    print(f"4. After insert: {fruits}")
    
    # 5. Remove "banana"
    fruits.remove("banana")
    print(f"5. After remove: {fruits}")
    
    # 6. Sort alphabetically
    fruits.sort()
    print(f"6. After sort: {fruits}")
    
    # 7. Print length
    print(f"7. List length: {len(fruits)}")

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
    """
    # 1. Squares
    squares = [x**2 for x in range(1, 11)]
    print(f"1. Squares 1-10: {squares}")
    
    # 2. Even numbers
    evens = [x for x in range(1, 21) if x % 2 == 0]
    print(f"2. Even numbers 1-20: {evens}")
    
    # 3. Uppercase words
    words = ["hello", "world", "python"]
    uppercase_words = [word.upper() for word in words]
    print(f"3. Uppercase words: {uppercase_words}")
    
    # 4. Word lengths
    words2 = ["cat", "elephant", "dog", "butterfly"]
    word_lengths = [len(word) for word in words2]
    print(f"4. Word lengths: {word_lengths}")

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
    # Create tuple
    coordinates = (10, 20, 30)
    
    # 1. Print tuple and type
    print(f"1. coordinates: {coordinates}, type: {type(coordinates)}")
    
    # 2. First and last element
    print(f"2. First: {coordinates[0]}, Last: {coordinates[-1]}")
    
    # 3. Try to modify (will fail)
    print(f"3. Attempting to modify tuple...")
    try:
        coordinates[0] = 5
    except TypeError as e:
        print(f"   Error: {e}")
    
    # 4. Concatenate tuples
    new_coordinates = coordinates + (40, 50)
    print(f"4. Concatenated: {new_coordinates}")
    
    # 5. Unpack tuple
    x, y, z = coordinates
    print(f"5. Unpacked: x={x}, y={y}, z={z}")

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
    # Create dictionary
    student = {
        "name": "John Doe",
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Physics", "Computer Science"]
    }
    
    # 1. Print name
    print(f"1. Student name: {student['name']}")
    
    # 2. Add city
    student["city"] = "New York"
    print(f"2. After adding city: {student}")
    
    # 3. Update age
    student["age"] = 21
    print(f"3. After updating age: {student}")
    
    # 4. Remove grade
    del student["grade"]
    print(f"4. After removing grade: {student}")
    
    # 5. Print keys, values, and items
    print(f"5. Keys: {list(student.keys())}")
    print(f"   Values: {list(student.values())}")
    print(f"   Items: {list(student.items())}")

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
    inventory = {"apples": 10, "bananas": 5, "oranges": 8, "grapes": 15}
    
    # 1. Check existence
    print(f"1. 'apples' in inventory: {'apples' in inventory}")
    
    # 2. Get bananas value
    bananas_value = inventory.get("bananas")
    print(f"2. bananas value: {bananas_value}")
    
    # 3. Get pears with default
    pears_value = inventory.get("pears", 0)
    print(f"3. pears value (with default): {pears_value}")
    
    # 4. Print all items
    print(f"4. All items:")
    for item, quantity in inventory.items():
        print(f"   {item}: {quantity}")
    
    # 5. Create dictionary with defaults
    new_fruits = ["mango", "kiwi", "peach"]
    default_dict = {fruit: 0 for fruit in new_fruits}
    print(f"5. Default dictionary: {default_dict}")

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
    4. Symmetric difference
    5. Check if set_a is a subset of set_b
    6. Add 9 to set_a
    7. Remove 1 from set_a
    """
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    
    # 1. Union
    union = set_a | set_b
    print(f"1. Union: {union}")
    
    # 2. Intersection
    intersection = set_a & set_b
    print(f"2. Intersection: {intersection}")
    
    # 3. Difference
    difference = set_a - set_b
    print(f"3. Difference (A - B): {difference}")
    
    # 4. Symmetric difference
    sym_diff = set_a ^ set_b
    print(f"4. Symmetric difference: {sym_diff}")
    
    # 5. Subset check
    is_subset = set_a.issubset(set_b)
    print(f"5. Is A a subset of B? {is_subset}")
    
    # 6. Add 9
    set_a.add(9)
    print(f"6. After adding 9: {set_a}")
    
    # 7. Remove 1
    set_a.remove(1)
    print(f"7. After removing 1: {set_a}")

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
    school = {
        "name": "Python High School",
        "students": [
            {"name": "Alice", "grade": 9, "subjects": ["Math", "Science"]},
            {"name": "Bob", "grade": 10, "subjects": ["English", "History"]},
            {"name": "Charlie", "grade": 9, "subjects": ["Math", "Art"]}
        ],
        "teachers": ["Mr. Smith", "Ms. Johnson", "Dr. Brown"]
    }
    
    # 1. Print school name
    print(f"1. School name: {school['name']}")
    
    # 2. Print all student names
    student_names = [student["name"] for student in school["students"]]
    print(f"2. Student names: {student_names}")
    
    # 3. Print Bob's subjects
    bob = next(student for student in school["students"] if student["name"] == "Bob")
    print(f"3. Bob's subjects: {bob['subjects']}")
    
    # 4. Add new student
    new_student = {"name": "Diana", "grade": 11, "subjects": ["Physics", "Chemistry"]}
    school["students"].append(new_student)
    print(f"4. Added Diana. Total students now: {len(school['students'])}")
    
    # 5. Total number of students
    print(f"5. Total students: {len(school['students'])}")
    
    # 6. Find students in grade 9
    grade_9_students = [student["name"] for student in school["students"] if student["grade"] == 9]
    print(f"6. Students in grade 9: {grade_9_students}")

# ==============================================================================
# EXERCISE 8: List Manipulation Algorithms
# ==============================================================================

def exercise_8():
    """
    Implement functions WITHOUT using built-in methods like sum(), max(), min().
    """
    def calculate_sum(numbers):
        total = 0
        for num in numbers:
            total += num
        return total
    
    def find_max(numbers):
        if not numbers:
            return None
        max_num = numbers[0]
        for num in numbers[1:]:
            if num > max_num:
                max_num = num
        return max_num
    
    def find_min(numbers):
        if not numbers:
            return None
        min_num = numbers[0]
        for num in numbers[1:]:
            if num < min_num:
                min_num = num
        return min_num
    
    def reverse_list(items):
        reversed_items = []
        for i in range(len(items) - 1, -1, -1):
            reversed_items.append(items[i])
        return reversed_items
    
    def count_occurrences(items, target):
        count = 0
        for item in items:
            if item == target:
                count += 1
        return count
    
    # Test the functions
    numbers = [3, 7, 2, 9, 1, 7, 4, 7]
    print(f"Test data: {numbers}")
    print(f"Sum: {calculate_sum(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")
    print(f"Reversed: {reverse_list(numbers)}")
    print(f"Count of 7: {count_occurrences(numbers, 7)}")

# ==============================================================================
# EXERCISE 9: Dictionary Counting
# ==============================================================================

def exercise_9():
    """
    Given a string: "the quick brown fox jumps over the lazy dog"
    
    Use a dictionary to count letter and word frequencies.
    """
    text = "the quick brown fox jumps over the lazy dog"
    
    # 1. Letter frequency (ignore spaces)
    letter_freq = {}
    for char in text.lower():
        if char != ' ':  # Ignore spaces
            letter_freq[char] = letter_freq.get(char, 0) + 1
    
    print("1. Letter frequency:")
    for letter, count in sorted(letter_freq.items()):
        print(f"   '{letter}': {count}")
    
    # 2. Word frequency
    words = text.lower().split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print("\n2. Word frequency:")
    for word, count in word_freq.items():
        print(f"   '{word}': {count}")
    
    # 3. Most common letter
    most_common_letter = max(letter_freq.items(), key=lambda x: x[1])
    print(f"\n3. Most common letter: '{most_common_letter[0]}' ({most_common_letter[1]} times)")
    
    # 4. Most common word
    most_common_word = max(word_freq.items(), key=lambda x: x[1])
    print(f"4. Most common word: '{most_common_word[0]}' ({most_common_word[1]} times)")

# ==============================================================================
# EXERCISE 10: Set Operations for Data Analysis
# ==============================================================================

def exercise_10():
    """
    Analyze two lists of students.
    """
    math_students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    science_students = ["Charlie", "David", "Frank", "Grace", "Henry"]
    
    # Convert to sets for set operations
    math_set = set(math_students)
    science_set = set(science_students)
    
    print(f"Math students: {math_students}")
    print(f"Science students: {science_students}")
    
    # 1. Students taking both
    both = math_set & science_set
    print(f"\n1. Students taking both: {both}")
    
    # 2. Students taking only math
    only_math = math_set - science_set
    print(f"2. Students taking only math: {only_math}")
    
    # 3. Students taking only science
    only_science = science_set - math_set
    print(f"3. Students taking only science: {only_science}")
    
    # 4. All unique students
    all_students = math_set | science_set
    print(f"4. All unique students: {all_students}")
    
    # 5. Students taking exactly one subject
    one_subject = math_set ^ science_set
    print(f"5. Students taking exactly one subject: {one_subject}")

# ==============================================================================
# EXERCISE 11: List Filtering and Transformation
# ==============================================================================

def exercise_11():
    """
    Filter mixed list by data type.
    """
    mixed = [10, "hello", 3.14, True, "world", 42, False, "python", 2.5]
    
    strings_list = [item for item in mixed if isinstance(item, str)]
    numbers_list = [item for item in mixed if isinstance(item, (int, float)) and not isinstance(item, bool)]
    booleans_list = [item for item in mixed if isinstance(item, bool)]
    
    print(f"Original mixed list: {mixed}")
    print(f"Strings: {strings_list}")
    print(f"Numbers: {numbers_list}")
    print(f"Booleans: {booleans_list}")

# ==============================================================================
# EXERCISE 12: Dictionary of Lists
# ==============================================================================

def exercise_12():
    """
    Analyze a gradebook.
    """
    grades = {
        "Alice": [85, 90, 78, 92],
        "Bob": [75, 82, 88, 79],
        "Charlie": [95, 89, 93, 97],
        "Diana": [70, 68, 75, 72]
    }
    
    # 1. Each student's average
    print("1. Student averages:")
    averages = {}
    for student, student_grades in grades.items():
        avg = sum(student_grades) / len(student_grades)
        averages[student] = avg
        print(f"   {student}: {avg:.2f}")
    
    # 2. Class average
    all_grades = []
    for student_grades in grades.values():
        all_grades.extend(student_grades)
    class_avg = sum(all_grades) / len(all_grades)
    print(f"\n2. Class average: {class_avg:.2f}")
    
    # 3. Student with highest average
    top_student = max(averages.items(), key=lambda x: x[1])
    print(f"3. Highest average: {top_student[0]} ({top_student[1]:.2f})")
    
    # 4. Students above 85
    above_85 = [student for student, avg in averages.items() if avg > 85]
    print(f"4. Students with average above 85: {above_85}")

# ==============================================================================
# EXERCISE 13: Matrix Operations
# ==============================================================================

def exercise_13():
    """
    Perform matrix operations.
    """
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Matrix:")
    for row in matrix:
        print(f"  {row}")
    
    # 1. Element at row 1, column 2
    print(f"\n1. Element at [1][2]: {matrix[1][2]}")
    
    # 2. First row
    print(f"2. First row: {matrix[0]}")
    
    # 3. Second column
    second_col = [row[1] for row in matrix]
    print(f"3. Second column: {second_col}")
    
    # 4. Sum of all elements
    total_sum = sum(sum(row) for row in matrix)
    print(f"4. Sum of all elements: {total_sum}")
    
    # 5. Sum of main diagonal
    diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    print(f"5. Sum of main diagonal: {diagonal_sum}")
    
    # 6. Transpose matrix
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print(f"6. Transposed matrix:")
    for row in transpose:
        print(f"   {row}")

# ==============================================================================
# EXERCISE 14: Shopping Cart
# ==============================================================================

def exercise_14():
    """
    Implement a shopping cart.
    """
    def add_item(cart, name, price, quantity):
        cart[name] = {"price": price, "quantity": quantity}
        print(f"Added {quantity} x {name} at ${price:.2f} each")
    
    def remove_item(cart, name):
        if name in cart:
            del cart[name]
            print(f"Removed {name} from cart")
        else:
            print(f"{name} not in cart")
    
    def update_quantity(cart, name, quantity):
        if name in cart:
            cart[name]["quantity"] = quantity
            print(f"Updated {name} quantity to {quantity}")
        else:
            print(f"{name} not in cart")
    
    def calculate_total(cart):
        total = 0
        for item, details in cart.items():
            total += details["price"] * details["quantity"]
        return total
    
    def display_cart(cart):
        if not cart:
            print("Cart is empty")
            return
        
        print("\n" + "=" * 50)
        print("SHOPPING CART")
        print("-" * 50)
        print(f"{'Item':<15} {'Price':>8} {'Qty':>6} {'Total':>10}")
        print("-" * 50)
        
        total = 0
        for item, details in cart.items():
            item_total = details["price"] * details["quantity"]
            total += item_total
            print(f"{item:<15} ${details['price']:>7.2f} {details['quantity']:>6} ${item_total:>9.2f}")
        
        print("-" * 50)
        print(f"{'TOTAL':<15} {'':>15} ${total:>9.2f}")
        print("=" * 50)
    
    # Test the shopping cart
    cart = {}
    print("Testing Shopping Cart:")
    print("-" * 30)
    
    add_item(cart, "Python Book", 29.99, 2)
    add_item(cart, "Coffee Mug", 15.50, 1)
    add_item(cart, "Stickers", 2.99, 5)
    
    display_cart(cart)
    
    print(f"\nTotal cost: ${calculate_total(cart):.2f}")
    
    update_quantity(cart, "Python Book", 3)
    remove_item(cart, "Coffee Mug")
    
    display_cart(cart)

# ==============================================================================
# EXERCISE 15: Data Structure Conversion
# ==============================================================================

def exercise_15():
    """
    Convert between different data structures.
    """
    # Given data
    people_list = [("Alice", 25, "NYC"), ("Bob", 30, "LA"), ("Charlie", 35, "Chicago")]
    people_dict = {"Alice": (25, "NYC"), "Bob": (30, "LA"), "Charlie": (35, "Chicago")}
    
    print("Original data:")
    print(f"people_list: {people_list}")
    print(f"people_dict: {people_dict}")
    
    # 1. Convert list to dict
    list_to_dict = {person[0]: (person[1], person[2]) for person in people_list}
    print(f"\n1. List to dict: {list_to_dict}")
    
    # 2. Convert dict to list
    dict_to_list = [(name, age, city) for name, (age, city) in people_dict.items()]
    print(f"2. Dict to list: {dict_to_list}")
    
    # 3. Set of all cities
    cities = {person[2] for person in people_list}
    print(f"3. All cities: {cities}")
    
    # 4. People older than 28
    older_than_28 = [person[0] for person in people_list if person[1] > 28]
    print(f"4. People older than 28: {older_than_28}")
    
    # 5. Group people by city
    people_by_city = {}
    for name, age, city in people_list:
        if city not in people_by_city:
            people_by_city[city] = []
        people_by_city[city].append((name, age))
    
    print(f"5. People by city: {people_by_city}")

# ==============================================================================
# MAIN FUNCTION TO RUN ALL SOLUTIONS
# ==============================================================================

def main():
    """
    Run all exercise solutions in sequence.
    """
    print("Module 04: Data Structures - Solutions")
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