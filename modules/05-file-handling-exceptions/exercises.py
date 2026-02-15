"""
Module 05: File Handling and Exceptions - Exercises

Practice working with files and handling exceptions.
Try to solve these exercises without looking at the solutions first!
"""

import os

# ==============================================================================
# EXERCISE 1: Basic File Writing
# ==============================================================================

def exercise_1():
    """
    Create a file called 'notes.txt' and write the following lines to it:
    - "Python is awesome!"
    - "File handling is useful."
    - "I'm learning to write files."
    
    Each line should be on a separate line in the file.
    After writing, read the file and print its contents.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 2: Reading and Processing
# ==============================================================================

def exercise_2():
    """
    Create a file called 'numbers.txt' with the following numbers (one per line):
    10
    20
    30
    40
    50
    
    Then write a program that:
    1. Reads all numbers from the file
    2. Calculates their sum and average
    3. Appends the results to the end of the file in the format:
       "Sum: [sum]"
       "Average: [average]"
    
    Handle any potential file errors.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 3: Student Grades System
# ==============================================================================

def exercise_3():
    """
    Create a student grades system that:
    1. Asks the user for a student name and grade
    2. Appends this information to 'grades.txt' in format: "name,grade"
    3. Allows the user to enter multiple students (type 'done' to finish)
    4. After finishing, reads the file and displays:
       - All students and their grades
       - Class average
       - Highest and lowest grade
    
    Handle exceptions for invalid grades (should be 0-100).
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 4: File Copy with Error Handling
# ==============================================================================

def exercise_4():
    """
    Write a function that copies the contents of one file to another.
    
    The function should:
    1. Ask the user for source and destination filenames
    2. Check if source file exists before attempting to read
    3. Handle permission errors
    4. Ask for confirmation before overwriting an existing destination file
    5. Provide appropriate success/error messages
    
    Test your function with different scenarios.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 5: Word Counter
# ==============================================================================

def exercise_5():
    """
    Write a program that analyzes a text file and provides statistics:
    
    1. Ask the user for a filename
    2. Count and display:
       - Total number of lines
       - Total number of words
       - Total number of characters (including spaces)
       - Average word length
       - The most common word (case-insensitive)
    
    Handle the case where the file doesn't exist.
    
    Test with a sample text file you create.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 6: Exception Handling Calculator
# ==============================================================================

def exercise_6():
    """
    Create a simple calculator that handles exceptions:
    
    The program should:
    1. Ask the user for two numbers and an operation (+, -, *, /)
    2. Perform the calculation
    3. Handle these specific exceptions:
       - ValueError: if user enters non-numeric input
       - ZeroDivisionError: if trying to divide by zero
       - KeyError: if user enters invalid operation
    4. Keep asking until the user types 'quit'
    
    Use try/except/else/finally blocks appropriately.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 7: Configuration File Parser
# ==============================================================================

def exercise_7():
    """
    Create a simple configuration file parser.
    
    Given a file 'config.txt' with content like:
    ```
    # This is a comment
    database=localhost
    port=5432
    username=admin
    password=secret
    debug=True
    ```
    
    Write a function that:
    1. Reads the config file
    2. Ignores lines that start with '#' (comments)
    3. Splits each line by '=' to get key-value pairs
    4. Returns a dictionary with the configuration
    5. Handles file not found errors
    
    Test with a sample config file.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 8: Log File Analyzer
# ==============================================================================

def exercise_8():
    """
    Create a log file analyzer.
    
    Assume you have a log file 'app.log' with lines like:
    ```
    2024-01-15 10:30:45 - INFO - Application started
    2024-01-15 10:31:22 - ERROR - Database connection failed
    2024-01-15 10:32:10 - WARNING - Memory usage high
    2024-01-15 10:33:05 - INFO - Request processed
    ```
    
    Write functions to:
    1. Count occurrences of each log level (INFO, ERROR, WARNING)
    2. Extract all ERROR messages
    3. Find the most frequent type of log entry
    4. Create a summary report file 'summary.txt'
    
    Handle file not found and empty file cases.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 9: CSV Data Processor
# ==============================================================================

def exercise_9():
    """
    Process a CSV file containing employee data.
    
    Create a file 'employees.csv' with format:
    ```
    Name,Department,Salary,Years
    Alice,Engineering,75000,5
    Bob,Marketing,65000,3
    Charlie,Engineering,80000,7
    Diana,HR,55000,2
    ```
    
    Write functions to:
    1. Read the CSV and calculate average salary by department
    2. Find the employee with the highest salary
    3. Calculate total years of experience in each department
    4. Add a new employee record to the file
    5. Handle malformed lines gracefully
    
    Use proper exception handling throughout.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 10: Custom Exception - InsufficientFundsError
# ==============================================================================

def exercise_10():
    """
    Create a custom exception called InsufficientFundsError.
    
    Then implement a BankAccount class with:
    - __init__(self, owner, balance=0)
    - deposit(self, amount)
    - withdraw(self, amount)
    - get_balance(self)
    
    The withdraw method should raise InsufficientFundsError with
    an appropriate message if there aren't enough funds.
    
    Test your class with various scenarios and handle the custom exception.
    """
    # TODO: Create your custom exception and BankAccount class here
    pass

# ==============================================================================
# EXERCISE 11: Multi-File Search Tool
# ==============================================================================

def exercise_11():
    """
    Create a search tool that searches for a string in multiple files.
    
    The program should:
    1. Ask the user for a directory path and search term
    2. Search all .txt files in that directory for the term
    3. For each file, display:
       - Filename
       - Line numbers where the term appears
       - The actual line content
    4. Handle:
       - Directory not found
       - Permission errors
       - No .txt files found
    
    Use os.listdir() to get files in a directory.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 12: File Backup System
# ==============================================================================

def exercise_12():
    """
    Create a simple file backup system.
    
    Write a function that:
    1. Takes a filename as input
    2. Creates a backup by copying the file to 'filename.backup'
    3. If the backup file already exists, ask user whether to:
       - Overwrite
       - Create a new version (filename.backup.1, .backup.2, etc.)
       - Cancel
    4. Handle all file-related exceptions
    
    Test with different files and scenarios.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 13: Data Validation with Exceptions
# ==============================================================================

def exercise_13():
    """
    Create a data validation system for user registration.
    
    Ask the user for:
    - Username (at least 3 characters, no spaces)
    - Email (must contain @ and .)
    - Age (must be 18-120)
    - Password (at least 8 characters, with 1 number and 1 uppercase)
    
    Create custom exceptions for each validation failure.
    Validate all inputs and raise appropriate exceptions.
    Handle all exceptions and display user-friendly error messages.
    """
    # TODO: Write your code with custom exceptions here
    pass

# ==============================================================================
# EXERCISE 14: File Organizer
# ==============================================================================

def exercise_14():
    """
    Create a file organizer that sorts files into folders by extension.
    
    The program should:
    1. Ask for a directory path
    2. Scan all files in that directory
    3. Create subfolders based on file extensions (e.g., 'txt', 'pdf', 'jpg')
    4. Move files into their respective folders
    5. Handle cases where:
       - Files with no extension go to 'others' folder
       - Folders already exist
       - Permission errors occur
       - Files with same name exist in destination
    
    Use os.mkdir(), os.rename(), and proper exception handling.
    """
    # TODO: Write your code here
    pass

# ==============================================================================
# EXERCISE 15: Journal with Exception Logging
# ==============================================================================

def exercise_15():
    """
    Create a personal journal program with exception logging.
    
    Features:
    1. Add new entries (date, title, content)
    2. View all entries
    3. Search entries by date or keyword
    4. Save entries to 'journal.json' file
    5. Load entries on startup
    
    Exception logging:
    - Create a decorator that logs any exceptions to 'error.log'
    - Include timestamp, exception type, and function name
    - Use this decorator on all major functions
    
    Handle JSON decode errors, file not found, etc.
    """
    # TODO: Write your code with exception logging decorator here
    pass

# ==============================================================================
# MAIN FUNCTION TO RUN ALL EXERCISES
# ==============================================================================

def main():
    """
    Run all exercises in sequence.
    Uncomment the exercises you want to test.
    """
    print("Module 05: File Handling and Exceptions - Exercises")
    print("=" * 50)
    
    # Uncomment the exercises you want to run:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()
    # exercise_11()
    # exercise_12()
    # exercise_13()
    # exercise_14()
    # exercise_15()

if __name__ == "__main__":
    main()