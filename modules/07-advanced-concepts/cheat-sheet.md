# Advanced Concepts Cheat Sheet

## List Comprehensions

Short syntax for creating lists.

```python
# [expression for item in iterable if condition]
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]          # [1, 4, 9, 16]
evens = [n for n in numbers if n % 2 == 0] # [2, 4]
```

## Lambda Functions

Anonymous, single-expression functions.

```python
# lambda arguments: expression
double = lambda x: x * 2
print(double(5)) # 10

# Often used with map(), filter(), sorted()
points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda p: p[1]) # Sort by 2nd element
```

## Decorators

Wrappers to modify function behavior.

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

## Generators

Functions that yield values one at a time (lazy evaluation).

```python
def my_gen():
    yield 1
    yield 2
    yield 3

for val in my_gen():
    print(val)
```
