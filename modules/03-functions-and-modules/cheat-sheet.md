# Module 03 Cheat Sheet: Functions and Modules

## Definitions

- **Function**: A block of reusable code.
- **Parameter**: A variable listed inside the parentheses in the function definition.
- **Argument**: The value sent to the function when it is called.
- **Return Value**: The result that a function sends back to the caller.

## Syntax

```python
def function_name(parameter1, parameter2):
    # Function body
    result = parameter1 + parameter2
    return result
```

## Types of Arguments

### Positional Arguments

Order matters.

```python
func(10, 20)
```

### Keyword Arguments

Order doesn't matter if names are specified.

```python
func(parameter2=20, parameter1=10)
```

### Default Arguments

Arguments that assume a default value if not provided.

```python
def greet(name="User"):
    print(f"Hello, {name}")
```

## Scope

- **Local Scope**: Variables defined inside a function. Only accessible within that function.
- **Global Scope**: Variables defined in the main body of the script. Accessible everywhere (for reading). To modify a global variable inside a function, use the `global` keyword.

## Lambda Functions

Small anonymous functions.

```python
# Syntax: lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 3))  # 8
```

## Modules

Importing external code.

```python
import math
print(math.pi)

from math import sqrt
print(sqrt(16))

import random as rnd  # Alias
print(rnd.randint(1, 10))
```
