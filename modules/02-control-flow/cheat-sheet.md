# Module 02 Cheat Sheet: Control Flow

## Conditional Statements

### if / elif / else

```python
if condition:
    # code to run if condition is True
elif another_condition:
    # code to run if another_condition is True
else:
    # code to run if no conditions are True
```

### Logical Operators

- `and`: Both must be True (`True and True`)
- `or`: At least one must be True (`True or False`)
- `not`: Inverts the boolean value (`not True` is `False`)

---

## Loops

### for loop

Iterates over a sequence (list, string, range).

```python
for item in sequence:
    print(item)
```

### range() function

Generates a sequence of numbers.

- `range(stop)`: 0 to stop-1
- `range(start, stop)`: start to stop-1
- `range(start, stop, step)`: increments by step

```python
# 0, 1, 2, 3, 4
range(5)

# 2, 3, 4
range(2, 5)

# 0, 2, 4, 6, 8
range(0, 10, 2)
```

### while loop

Repeats as long as the condition is True.

```python
while condition:
    # code
    # update condition to avoid infinite loop
```

---

## Loop Control

- **break**: Exits the loop immediately.
- **continue**: Skips the rest of the current iteration and continues with the next.
- **pass**: Does nothing (placeholder).

```python
for i in range(10):
    if i == 5:
        break    # Stops loop at 5
    if i % 2 == 0:
        continue # Skips even numbers
    print(i)
```
