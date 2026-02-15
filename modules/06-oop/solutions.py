"""
Module 06: OOP - Solutions
"""

print("--- Module 06 Solutions ---")

# ==============================================================================
# Exercise 1: Rectangle Class
# ==============================================================================
print("\nExercise 1: Rectangle Class")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(f"Rectangle (5x3) - Area: {rect.area()}, Perimeter: {rect.perimeter()}")


# ==============================================================================
# Exercise 2: Bank Account
# ==============================================================================
print("\nExercise 2: Bank Account")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
            
    def get_balance(self):
        return self.balance

acct = BankAccount("Alice", 100)
acct.deposit(50)
acct.withdraw(30)
acct.withdraw(200)
print(f"Final Balance: ${acct.get_balance()}")
