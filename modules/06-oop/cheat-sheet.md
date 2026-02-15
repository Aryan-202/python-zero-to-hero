# OOP Cheat Sheet

## Class Definition

A blueprint for creating objects.

```python
class MyClass:
    # Class Attribute (shared by all instances)
    species = "Human"

    # Constructor (Initializer)
    def __init__(self, name, age):
        # Instance Attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance Method
    def greet(self):
        return f"Hi, I'm {self.name}"

# Creating an Object
p1 = MyClass("Alice", 30)
```

## Accessing Members

```python
print(p1.name)   # Alice
print(p1.greet()) # Hi, I'm Alice
```

## Inheritance

Child class inherits from Parent class.

```python
class Parent:
    def func(self):
        print("Parent")

class Child(Parent):
    def func(self):
        print("Child (Override)")
```

## Concepts

- **Encapsulation**: Bundling data and methods (using `self`).
- **Inheritance**: reusing code from parent classes.
- **Polymorphism**: Different classes responding to same method calls (e.g. `len()` works on strings and lists).
