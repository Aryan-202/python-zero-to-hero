# Python Data Structures Cheat Sheet

## Lists `[]`
```python
# Creation
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

# Common Methods
fruits.append("orange")        # Add to end
fruits.insert(1, "grape")      # Insert at index
fruits.remove("banana")        # Remove first occurrence
popped = fruits.pop()          # Remove and return last
popped = fruits.pop(1)         # Remove and return index
fruits.sort()                  # Sort in place
fruits.reverse()               # Reverse in place
index = fruits.index("apple")  # Find index
count = fruits.count("apple")  # Count occurrences
fruits.extend(["kiwi", "mango"]) # Add multiple

# Indexing and Slicing
first = fruits[0]               # First element
last = fruits[-1]               # Last element
first_three = fruits[:3]        # First three
last_two = fruits[-2:]          # Last two
every_other = fruits[::2]       # Every second element

# Operations
length = len(fruits)
exists = "apple" in fruits
combined = fruits + ["pear", "peach"]
repeated = fruits * 2