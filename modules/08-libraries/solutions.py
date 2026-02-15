"""
Module 08: External Libraries - Solutions
"""

import json

print("--- Module 08 Solutions ---")

# ==============================================================================
# Exercise 1: JSON Parsing
# ==============================================================================
print("\nExercise 1: JSON Parsing")

json_data = '{"name": "Alice", "age": 30, "city": "Paris", "hobbies": ["reading", "painting", "coding"]}'

def parse_and_print(json_string):
    data = json.loads(json_string)
    print(f"City: {data['city']}")
    print(f"Second Hobby: {data['hobbies'][1]}")

parse_and_print(json_data)


# ==============================================================================
# Exercise 2: Create JSON
# ==============================================================================
print("\nExercise 2: Create JSON")

def create_book_json():
    book = {
        "title": "The Python Journey",
        "author": "Guido van Rossum",
        "year": 2024,
        "is_published": True
    }
    
    json_str = json.dumps(book, indent=4)
    print(json_str)

create_book_json()
