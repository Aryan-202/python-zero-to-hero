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
```

## Tuples `()`

Immutable sequences.

```python
# Creation
coordinates = (10, 20)
colors = ("red", "green", "blue")
single = (1,)  # Note the comma

# Packing and Unpacking
point = 1, 2, 3   # Packing
x, y, z = point   # Unpacking

# Methods
count = colors.count("red")
index = colors.index("green")
```

## Dictionaries `{key: value}`

Key-Value pairs. Keys must be immutable.

```python
# Creation
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing
name = person["name"]
age = person.get("age", 0)  # Default if missing

# Modifying
person["email"] = "alice@example.com"  # Add/Update
del person["city"]                     # Remove
popped = person.pop("age")             # Remove and return value

# Methods
keys = person.keys()
values = person.values()
items = person.items()  # (key, value) pairs

# Looping
for key, value in person.items():
    print(key, value)
```

## Sets `{}`

Unordered, unique elements.

```python
# Creation
numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
empty_set = set()          # {} creates a dict

# Operations
numbers.add(5)
numbers.remove(1)      # Raises error if missing
numbers.discard(1)     # No error if missing

# Set Math
a = {1, 2, 3}
b = {3, 4, 5}

union = a | b          # {1, 2, 3, 4, 5}
intersection = a & b   # {3}
difference = a - b     # {1, 2}
symmetric_diff = a ^ b # {1, 2, 4, 5}
```

## List Comprehensions

Concise way to create lists.

```python
# [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```
