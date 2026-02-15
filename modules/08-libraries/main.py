"""
Module 08: Working with External Libraries
"""

import json
# Usually we would import requests, pandas etc. here.
# For this vanilla course structure, we'll stick to stdlib json to simulate API data.

print("📦 Module 08: External Libraries")
print("=" * 50)

# Simulating JSON data handling (often used with APIs)
print("\n1. JSON Data Handling")
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

json_str = json.dumps(data, indent=4)
print("Serialized JSON:")
print(json_str)

parsed_data = json.loads(json_str)
print(f"\nParsed back: Name is {parsed_data['name']}")

print("\n(In a real scenario, you would use 'pip install requests' to fetch data from the web!)")
