# File Handling & Exceptions Cheat Sheet

## Opening Files

Use the `with` statement to handle files safely.

```python
with open("filename.txt", "mode") as f:
    # do operations
```

### Modes

- `'r'`: **Read** (default). Error if file doesn't exist.
- `'w'`: **Write**. Creates new file or overwrites existing.
- `'a'`: **Append**. Adds to end of file. Creates new if missing.
- `'r+'`: Read and Write.

## Reading

```python
content = f.read()        # Read entire file
line = f.readline()       # Read one line
lines = f.readlines()     # Read all lines into a list
```

## Writing

```python
f.write("Hello\n")        # Write string
f.writelines(list_of_strings)
```

## Exception Handling

Handle errors gracefully to prevent crashes.

```python
try:
    # Risky code
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific error
    print("Can't divide by zero!")
except Exception as e:
    # Handle any other error
    print(f"Error: {e}")
else:
    # Runs if NO exception occurred
    print("Success!")
finally:
    # Runs NO MATTER WHAT (cleanup)
    print("Done.")
```

### Common Exceptions

- `FileNotFoundError`
- `ValueError`
- `TypeError`
- `ZeroDivisionError`
- `IndexError`
- `KeyError`
