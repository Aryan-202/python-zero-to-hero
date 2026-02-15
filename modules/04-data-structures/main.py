"""
Module 04: Data Structures

This module covers Python's built-in data structures:
- Lists: ordered, mutable sequences
- Tuples: ordered, immutable sequences
- Dictionaries: key-value pairs
- Sets: unordered collections of unique elements
"""

print("📚 Module 04: Data Structures")
print("=" * 50)

# ==============================================================================
# 1. LISTS - ORDERED, MUTABLE SEQUENCES
# ==============================================================================

print("\n1. LISTS")
print("-" * 30)

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", 3.14, True]
empty_list = []

print(f"Fruits list: {fruits}")
print(f"Numbers list: {numbers}")
print(f"Mixed list: {mixed}")
print(f"Empty list: {empty_list}")

# List indexing (0-based)
print(f"\nList indexing:")
print(f"  First fruit: {fruits[0]}")
print(f"  Last fruit: {fruits[-1]}")
print(f"  Second to last: {fruits[-2]}")

# List slicing
print(f"\nList slicing:")
print(f"  First two: {fruits[0:2]}")
print(f"  From index 1 to end: {fruits[1:]}")
print(f"  Up to index 2: {fruits[:2]}")
print(f"  Every other element: {numbers[::2]}")
print(f"  Reversed list: {numbers[::-1]}")

# List methods
print(f"\nList methods:")
fruits.append("grape")  # Add to end
print(f"  After append('grape'): {fruits}")

fruits.insert(1, "mango")  # Insert at index
print(f"  After insert(1, 'mango'): {fruits}")

fruits.remove("banana")  # Remove by value
print(f"  After remove('banana'): {fruits}")

popped = fruits.pop()  # Remove and return last item
print(f"  Popped item: {popped}")
print(f"  After pop(): {fruits}")

popped_index = fruits.pop(1)  # Remove and return item at index
print(f"  Popped item at index 1: {popped_index}")
print(f"  After pop(1): {fruits}")

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print(f"\nList concatenation: {list1} + {list2} = {concatenated}")

repeated = list1 * 3
print(f"List repetition: {list1} * 3 = {repeated}")

print(f"Length of fruits: {len(fruits)}")
print(f"Does 'apple' exist? {'apple' in fruits}")

# Sorting lists
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nUnsorted list: {unsorted}")

unsorted.sort()  # In-place sort
print(f"After sort(): {unsorted}")

unsorted.sort(reverse=True)
print(f"After sort(reverse=True): {unsorted}")

words = ["banana", "apple", "Cherry", "date"]
words.sort(key=str.lower)  # Case-insensitive sort
print(f"Case-insensitive sort: {words}")

# List comprehension
print(f"\nList comprehension:")
squares = [x**2 for x in range(1, 11)]
print(f"  Squares 1-10: {squares}")

evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"  Even numbers 1-20: {evens}")

# ==============================================================================
# 2. TUPLES - ORDERED, IMMUTABLE SEQUENCES
# ==============================================================================

print("\n2. TUPLES")
print("-" * 30)

# Creating tuples
point = (10, 20)
rgb = (255, 128, 0)
person = ("Alice", 25, "Engineer")
single_element = (42,)  # Note the comma
empty_tuple = ()

print(f"Point tuple: {point}")
print(f"RGB tuple: {rgb}")
print(f"Person tuple: {person}")
print(f"Single element tuple: {single_element}")
print(f"Empty tuple: {empty_tuple}")

# Tuple indexing and slicing
print(f"\nTuple indexing:")
print(f"  First coordinate: {point[0]}")
print(f"  Second coordinate: {point[1]}")
print(f"  First two elements of person: {person[:2]}")

# Tuple unpacking
x, y = point
print(f"\nTuple unpacking: x={x}, y={y}")

name, age, job = person
print(f"  name={name}, age={age}, job={job}")

# Tuple immutability
print(f"\nTuple immutability:")
print(f"  Tuples cannot be changed after creation")
try:
    point[0] = 5  # This will raise an error
except TypeError as e:
    print(f"  Error when trying to modify: {e}")

# When to use tuples vs lists
print(f"\nWhen to use tuples:")
print("  • When data shouldn't change (coordinates, RGB values)")
print("  • As dictionary keys (lists can't be keys)")
print("  • For better performance with fixed data")
print("  • To represent fixed groups of related values")

# ==============================================================================
# 3. DICTIONARIES - KEY-VALUE PAIRS
# ==============================================================================

print("\n3. DICTIONARIES")
print("-" * 30)

# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": [85, 90, 78, 92]
}

print(f"Student dictionary:")
print(f"  {student}")

# Accessing values
print(f"\nAccessing values:")
print(f"  Name: {student['name']}")
print(f"  Age: {student.get('age')}")  # Using get() method
print(f"  GPA: {student.get('gpa', 'Not available')}")  # Default value

# Adding and modifying
student["city"] = "New York"  # Add new key-value pair
print(f"\nAfter adding city: {student}")

student["age"] = 21  # Modify existing value
print(f"After modifying age: {student}")

# Dictionary methods
print(f"\nDictionary methods:")
print(f"  Keys: {list(student.keys())}")
print(f"  Values: {list(student.values())}")
print(f"  Items: {list(student.items())}")

# Iterating through dictionaries
print(f"\nIterating through dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nDictionary comprehension: {squares_dict}")

# Nested dictionaries
school = {
    "name": "Python High School",
    "students": {
        "student1": {"name": "Alice", "grade": 9},
        "student2": {"name": "Bob", "grade": 10}
    },
    "teachers": ["Mr. Smith", "Ms. Johnson"]
}

print(f"\nNested dictionary:")
print(f"  School name: {school['name']}")
print(f"  First student: {school['students']['student1']['name']}")

# ==============================================================================
# 4. SETS - UNORDERED COLLECTIONS OF UNIQUE ELEMENTS
# ==============================================================================

print("\n4. SETS")
print("-" * 30)

# Creating sets
fruits_set = {"apple", "banana", "orange", "apple"}  # Duplicates are removed
numbers_set = set([1, 2, 3, 2, 1])  # Create from list
empty_set = set()  # Note: {} creates an empty dictionary

print(f"Fruits set (duplicates removed): {fruits_set}")
print(f"Numbers set from list: {numbers_set}")
print(f"Empty set: {empty_set}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Union
union = set_a | set_b  # or set_a.union(set_b)
print(f"Union (A | B): {union}")

# Intersection
intersection = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection}")

# Difference
difference = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A - B): {difference}")

# Symmetric difference
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric difference (A ^ B): {sym_diff}")

# Subset and superset
set_c = {1, 2, 3}
print(f"\nIs {set_c} a subset of {set_a}? {set_c.issubset(set_a)}")
print(f"Is {set_a} a superset of {set_c}? {set_a.issuperset(set_c)}")

# Set methods
print(f"\nSet methods:")
fruits_set.add("grape")
print(f"  After add('grape'): {fruits_set}")

fruits_set.remove("banana")  # Raises error if not found
print(f"  After remove('banana'): {fruits_set}")

fruits_set.discard("kiwi")  # No error if not found
print(f"  After discard('kiwi'): {fruits_set}")

popped = fruits_set.pop()  # Remove and return arbitrary element
print(f"  Popped element: {popped}")
print(f"  After pop(): {fruits_set}")

# ==============================================================================
# 5. PRACTICAL EXAMPLES
# ==============================================================================

print("\n5. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Word frequency counter
def word_frequency(text):
    """Count frequency of each word in text."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

text = "the cat in the hat sat on the mat"
freq = word_frequency(text)
print("Word frequency:")
for word, count in freq.items():
    print(f"  '{word}': {count}")

# Example 2: Remove duplicates while preserving order
def remove_duplicates_preserve_order(items):
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [3, 1, 2, 1, 3, 4, 2, 5, 4]
unique = remove_duplicates_preserve_order(numbers)
print(f"\nRemove duplicates from {numbers}:")
print(f"  Result: {unique}")

# Example 3: Student gradebook
gradebook = {
    "Alice": [85, 90, 78, 92],
    "Bob": [75, 82, 88, 79],
    "Charlie": [95, 89, 93, 97]
}

print(f"\nGradebook averages:")
for student, grades in gradebook.items():
    average = sum(grades) / len(grades)
    print(f"  {student}: {average:.2f}")

# Example 4: Finding common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]

common = set(list1) & set(list2) & set(list3)
print(f"\nCommon elements in all three lists: {common}")

# Example 5: Matrix as list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"\nMatrix:")
for row in matrix:
    print(f"  {row}")

# Calculate sum of diagonal
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
print(f"Sum of main diagonal: {diagonal_sum}")

# ==============================================================================
# 6. PERFORMANCE COMPARISONS
# ==============================================================================

print("\n6. PERFORMANCE COMPARISONS")
print("-" * 30)

import time

# List vs Set for membership testing
test_data = range(10000)
test_list = list(test_data)
test_set = set(test_data)

# Test list membership
start = time.time()
for i in range(1000):
    _ = 9999 in test_list
list_time = time.time() - start

# Test set membership
start = time.time()
for i in range(1000):
    _ = 9999 in test_set
set_time = time.time() - start

print(f"List membership test (1000 checks): {list_time:.4f} seconds")
print(f"Set membership test (1000 checks): {set_time:.4f} seconds")
print(f"Sets are {list_time/set_time:.1f}x faster for membership testing!")

# ==============================================================================
# 7. COMMON PITFALLS AND BEST PRACTICES
# ==============================================================================

print("\n7. COMMON PITFALLS AND BEST PRACTICES")
print("-" * 30)

# Pitfall 1: Modifying a list while iterating
print("\nPitfall 1: Modifying a list while iterating")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Wrong way - don't do this!
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)

# Right way - create a new list
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Correct approach - new list: {even_numbers}")

# Pitfall 2: Using mutable objects as default arguments
print("\nPitfall 2: Mutable default arguments")

def bad_append(item, list=[]):  # Don't do this!
    list.append(item)
    return list

print(f"First call: {bad_append(1)}")
print(f"Second call: {bad_append(2)}")  # List persists between calls!

def good_append(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list

print(f"First call: {good_append(1)}")
print(f"Second call: {good_append(2)}")  # Fresh list each time

# Pitfall 3: Copying vs referencing
print("\nPitfall 3: Copying vs referencing")
original = [1, 2, 3]
reference = original  # This creates a reference, not a copy
copy = original.copy()  # This creates a shallow copy

original[0] = 99
print(f"Original after modification: {original}")
print(f"Reference (affected): {reference}")
print(f"Copy (unaffected): {copy}")

# ==============================================================================
# NEXT STEPS
# ==============================================================================

print("\n" + "=" * 50)
print("NEXT STEPS")
print("=" * 50)

print("""
Great job learning about data structures! 🎉

Next, you should:
1. Complete the exercises in exercises.py
2. Check your solutions with solutions.py
3. Take the quiz in quiz.py
4. Review the cheat-sheet.md for quick reference
5. Move on to Module 05: File Handling and Exceptions

Key takeaways from this module:
• Lists are ordered, mutable sequences - great for collections that change
• Tuples are ordered, immutable - perfect for fixed data
• Dictionaries store key-value pairs for fast lookups
• Sets ensure uniqueness and provide mathematical set operations
• Choose the right data structure for your use case
• Be aware of performance implications

Remember: The right data structure can make your code simpler and faster!
""")

print("🚀 You're building strong Python fundamentals!")