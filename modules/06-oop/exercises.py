"""
Module 06: OOP - Exercises

Practice creating Classes and Objects.
"""

# ==============================================================================
# Exercise 1: Rectangle Class
# ==============================================================================
# Create a class named `Rectangle`.
# 1. The __init__ method should accept `width` and `height`.
# 2. Add a method `area()` that returns width * height.
# 3. Add a method `perimeter()` that returns 2 * (width + height).

class Rectangle:
    pass # Your code here

# Test
# rect = Rectangle(5, 3)
# print(f"Area: {rect.area()}")      # Should be 15
# print(f"Perimeter: {rect.perimeter()}") # Should be 16


# ==============================================================================
# Exercise 2: Bank Account
# ==============================================================================
# Create a class `BankAccount`.
# 1. __init__ accepts `owner` and optional `balance` (default 0).
# 2. method `deposit(amount)`: adds amount to balance.
# 3. method `withdraw(amount)`: subtracts amount if sufficient funds, else prints "Insufficient funds".
# 4. method `get_balance()`: returns current balance.

class BankAccount:
    pass # Your code here

# Test
# acct = BankAccount("Alice", 100)
# acct.deposit(50)
# acct.withdraw(20)
# acct.withdraw(200) # Should fail
# print(acct.get_balance())
