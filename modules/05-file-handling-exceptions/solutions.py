"""
Module 05: File Handling and Exceptions - Solutions

These are the solutions for the exercises in this module.
Try to solve the exercises yourself before looking here!
"""

import os
import json
from datetime import datetime
import traceback

# ==============================================================================
# EXERCISE 1: Basic File Writing
# ==============================================================================

def exercise_1():
    """
    Create a file called 'notes.txt' and write lines to it.
    """
    filename = 'notes.txt'
    
    # Write to file
    with open(filename, 'w') as file:
        file.write("Python is awesome!\n")
        file.write("File handling is useful.\n")
        file.write("I'm learning to write files.\n")
    print(f"✅ File '{filename}' written successfully")
    
    # Read and print contents
    print("\nFile contents:")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
    
    # Clean up
    os.remove(filename)
    print(f"✅ Cleaned up '{filename}'")

# ==============================================================================
# EXERCISE 2: Reading and Processing
# ==============================================================================

def exercise_2():
    """
    Read numbers from file, calculate sum and average, append results.
    """
    filename = 'numbers.txt'
    
    # Create file with numbers
    numbers = [10, 20, 30, 40, 50]
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(f"{num}\n")
    print(f"✅ Created '{filename}' with numbers")
    
    # Read and process numbers
    try:
        with open(filename, 'r') as file:
            numbers_read = []
            for line in file:
                numbers_read.append(int(line.strip()))
        
        # Calculate statistics
        total = sum(numbers_read)
        average = total / len(numbers_read)
        
        # Append results
        with open(filename, 'a') as file:
            file.write(f"\nSum: {total}\n")
            file.write(f"Average: {average:.2f}\n")
        
        print(f"✅ Processed numbers - Sum: {total}, Average: {average:.2f}")
        
        # Display final file content
        print("\nFinal file content:")
        with open(filename, 'r') as file:
            print(file.read())
            
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")
    except ValueError as e:
        print(f"❌ Error processing numbers: {e}")
    finally:
        # Clean up
        if os.path.exists(filename):
            os.remove(filename)
            print(f"✅ Cleaned up '{filename}'")

# ==============================================================================
# EXERCISE 3: Student Grades System
# ==============================================================================

def exercise_3():
    """
    Interactive student grades system.
    """
    filename = 'grades.txt'
    grades = []
    
    print("📚 Student Grades System")
    print("Enter student names and grades (type 'done' to finish)")
    
    # Collect grades
    while True:
        name = input("\nEnter student name (or 'done'): ").strip()
        if name.lower() == 'done':
            break
        
        try:
            grade = float(input(f"Enter grade for {name} (0-100): "))
            if 0 <= grade <= 100:
                grades.append((name, grade))
                # Append to file immediately
                with open(filename, 'a') as file:
                    file.write(f"{name},{grade}\n")
                print(f"✅ Added {name} with grade {grade}")
            else:
                print("❌ Grade must be between 0 and 100")
        except ValueError:
            print("❌ Invalid grade. Please enter a number.")
    
    # Display statistics
    if grades:
        print("\n" + "=" * 40)
        print("GRADE SUMMARY")
        print("=" * 40)
        
        all_grades = [grade for _, grade in grades]
        average = sum(all_grades) / len(all_grades)
        highest = max(all_grades)
        lowest = min(all_grades)
        
        print("\nAll students:")
        for name, grade in grades:
            print(f"  {name}: {grade}")
        
        print(f"\n📊 Class Average: {average:.2f}")
        print(f"📈 Highest Grade: {highest}")
        print(f"📉 Lowest Grade: {lowest}")
        
        # Find student with highest grade
        top_student = max(grades, key=lambda x: x[1])
        print(f"🏆 Top Student: {top_student[0]} with {top_student[1]}")
    
    # Clean up
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\n✅ Cleaned up '{filename}'")

# ==============================================================================
# EXERCISE 4: File Copy with Error Handling
# ==============================================================================

def exercise_4():
    """
    Copy file contents with error handling.
    """
    def copy_file(source, destination):
        """Copy source file to destination with error handling."""
        try:
            # Check if source exists
            if not os.path.exists(source):
                raise FileNotFoundError(f"Source file '{source}' not found")
            
            # Check if destination exists
            if os.path.exists(destination):
                response = input(f"File '{destination}' exists. Overwrite? (y/n): ")
                if response.lower() != 'y':
                    print("❌ Copy cancelled")
                    return False
            
            # Copy file
            with open(source, 'r') as src, open(destination, 'w') as dst:
                content = src.read()
                dst.write(content)
            
            print(f"✅ Successfully copied '{source}' to '{destination}'")
            return True
            
        except PermissionError:
            print(f"❌ Permission denied: Cannot access files")
        except FileNotFoundError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        return False
    
    # Test the function
    print("📋 File Copy Utility")
    print("-" * 30)
    
    # Create a test source file
    source = 'test_source.txt'
    with open(source, 'w') as f:
        f.write("This is a test file.\nIt contains some content.\nFor copying demonstration.")
    
    destination = 'test_destination.txt'
    
    # Test copying
    copy_file(source, destination)
    
    # Display copied content
    if os.path.exists(destination):
        print("\nCopied file content:")
        with open(destination, 'r') as f:
            print(f.read())
    
    # Test with non-existent file
    print("\nTesting with non-existent file:")
    copy_file('nonexistent.txt', destination)
    
    # Clean up
    for file in [source, destination]:
        if os.path.exists(file):
            os.remove(file)
    print(f"\n✅ Cleaned up test files")

# ==============================================================================
# EXERCISE 5: Word Counter
# ==============================================================================

def exercise_5():
    """
    Analyze a text file and provide statistics.
    """
    from collections import Counter
    
    # Create a sample text file
    filename = 'sample_text.txt'
    sample_text = """The quick brown fox jumps over the lazy dog.
    Python is a powerful programming language.
    It is used for web development, data science, and automation.
    The quick brown fox is a classic pangram.
    Programming in Python is fun and rewarding."""
    
    with open(filename, 'w') as f:
        f.write(sample_text)
    
    def analyze_file(filename):
        """Analyze text file and print statistics."""
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            
            # Initialize counters
            total_lines = len(lines)
            total_words = 0
            total_chars = 0
            all_words = []
            
            # Process each line
            for line in lines:
                total_chars += len(line)
                words = line.strip().split()
                total_words += len(words)
                all_words.extend([word.lower().strip('.,!?;:') for word in words])
            
            # Calculate average word length
            if all_words:
                avg_word_length = sum(len(word) for word in all_words) / len(all_words)
            else:
                avg_word_length = 0
            
            # Find most common word
            word_counts = Counter(all_words)
            most_common = word_counts.most_common(1)
            most_common_word = most_common[0] if most_common else ("None", 0)
            
            # Display results
            print(f"\n📊 File Analysis: '{filename}'")
            print("=" * 40)
            print(f"📝 Total lines: {total_lines}")
            print(f"🔤 Total words: {total_words}")
            print(f"📏 Total characters: {total_chars}")
            print(f"📐 Average word length: {avg_word_length:.2f}")
            print(f"🔥 Most common word: '{most_common_word[0]}' ({most_common_word[1]} times)")
            
            # Display word frequency
            print("\nWord frequency (top 5):")
            for word, count in word_counts.most_common(5):
                print(f"  '{word}': {count}")
            
        except FileNotFoundError:
            print(f"❌ File '{filename}' not found")
        except PermissionError:
            print(f"❌ Permission denied to read '{filename}'")
        except Exception as e:
            print(f"❌ Error analyzing file: {e}")
    
    # Analyze the file
    analyze_file(filename)
    
    # Test with non-existent file
    print("\nTesting with non-existent file:")
    analyze_file('nonexistent.txt')
    
    # Clean up
    os.remove(filename)
    print(f"\n✅ Cleaned up '{filename}'")

# ==============================================================================
# EXERCISE 6: Exception Handling Calculator
# ==============================================================================

def exercise_6():
    """
    Calculator with exception handling.
    """
    print("🧮 Exception Handling Calculator")
    print("Enter 'quit' to exit")
    print("-" * 40)
    
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter calculation (e.g., 5 + 3): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            # Parse input
            parts = user_input.split()
            if len(parts) != 3:
                print("❌ Invalid format. Use: number operator number")
                continue
            
            num1, op, num2 = parts
            
            # Convert to numbers
            num1 = float(num1)
            num2 = float(num2)
            
            # Check if operation is valid
            if op not in operations:
                raise KeyError(f"Invalid operator '{op}'. Use +, -, *, /")
            
            # Perform calculation
            result = operations[op](num1, num2)
            
            # Display result
            print(f"✅ Result: {num1} {op} {num2} = {result}")
            
        except ValueError:
            print("❌ Invalid number format. Please enter valid numbers.")
        except ZeroDivisionError:
            print("❌ Cannot divide by zero!")
        except KeyError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        else:
            # This executes if no exception occurred
            print("✅ Calculation successful!")
        finally:
            # This always executes
            print("─" * 40)

# ==============================================================================
# EXERCISE 7: Configuration File Parser
# ==============================================================================

def exercise_7():
    """
    Parse a configuration file.
    """
    # Create a sample config file
    config_content = """# Database configuration
database=localhost
port=5432
username=admin
password=secret

# Application settings
debug=True
max_connections=100
timeout=30

# This is a comment
# empty lines are skipped
"""
    
    config_file = 'config.txt'
    with open(config_file, 'w') as f:
        f.write(config_content)
    
    def parse_config(filename):
        """Parse configuration file into dictionary."""
        config = {}
        
        try:
            with open(filename, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parse key=value
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Convert value types
                        if value.lower() == 'true':
                            value = True
                        elif value.lower() == 'false':
                            value = False
                        elif value.isdigit():
                            value = int(value)
                        elif value.replace('.', '').isdigit():
                            value = float(value)
                        
                        config[key] = value
                    else:
                        print(f"⚠️ Warning: Line {line_num} has invalid format: {line}")
            
            return config
            
        except FileNotFoundError:
            print(f"❌ Config file '{filename}' not found")
            return None
        except Exception as e:
            print(f"❌ Error parsing config: {e}")
            return None
    
    # Parse and display config
    print("📋 Configuration Parser")
    print("-" * 30)
    
    config = parse_config(config_file)
    if config:
        print("\nParsed configuration:")
        for key, value in config.items():
            print(f"  {key}: {value} (type: {type(value).__name__})")
    
    # Clean up
    os.remove(config_file)
    print(f"\n✅ Cleaned up '{config_file}'")

# ==============================================================================
# EXERCISE 8: Log File Analyzer
# ==============================================================================

def exercise_8():
    """
    Analyze log file and generate summary.
    """
    # Create a sample log file
    log_content = """2024-01-15 10:30:45 - INFO - Application started
2024-01-15 10:31:22 - ERROR - Database connection failed
2024-01-15 10:32:10 - WARNING - Memory usage high
2024-01-15 10:33:05 - INFO - Request processed
2024-01-15 10:34:12 - ERROR - Failed to save data
2024-01-15 10:35:30 - INFO - User logged in
2024-01-15 10:36:45 - WARNING - CPU usage 90%
2024-01-15 10:37:20 - ERROR - Timeout occurred
2024-01-15 10:38:15 - INFO - Backup completed
"""
    
    log_file = 'app.log'
    summary_file = 'summary.txt'
    
    with open(log_file, 'w') as f:
        f.write(log_content)
    
    def analyze_log(filename):
        """Analyze log file and generate summary."""
        log_counts = {'INFO': 0, 'ERROR': 0, 'WARNING': 0}
        error_messages = []
        all_levels = []
        
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Parse log line
                    parts = line.split(' - ')
                    if len(parts) >= 3:
                        timestamp = parts[0]
                        level = parts[1]
                        message = ' - '.join(parts[2:])
                        
                        # Count by level
                        if level in log_counts:
                            log_counts[level] += 1
                            all_levels.append(level)
                        
                        # Collect error messages
                        if level == 'ERROR':
                            error_messages.append(f"{timestamp}: {message}")
            
            # Generate summary
            with open(summary_file, 'w') as f:
                f.write("LOG ANALYSIS SUMMARY\n")
                f.write("=" * 50 + "\n\n")
                
                f.write("Log Level Counts:\n")
                for level, count in log_counts.items():
                    f.write(f"  {level}: {count}\n")
                
                f.write(f"\nTotal Entries: {sum(log_counts.values())}\n")
                
                if error_messages:
                    f.write(f"\nERROR Messages ({len(error_messages)}):\n")
                    for msg in error_messages:
                        f.write(f"  - {msg}\n")
                
                # Find most frequent level
                if all_levels:
                    most_frequent = max(set(all_levels), key=all_levels.count)
                    f.write(f"\nMost frequent level: {most_frequent}\n")
            
            # Display results
            print("📊 Log Analysis Results:")
            for level, count in log_counts.items():
                print(f"  {level}: {count}")
            print(f"  Total: {sum(log_counts.values())}")
            
            if error_messages:
                print(f"\nError Messages ({len(error_messages)}):")
                for msg in error_messages[:3]:  # Show first 3
                    print(f"  - {msg}")
            
            print(f"\n✅ Summary written to '{summary_file}'")
            
        except FileNotFoundError:
            print(f"❌ Log file '{filename}' not found")
        except Exception as e:
            print(f"❌ Error analyzing log: {e}")
    
    # Analyze the log
    analyze_log(log_file)
    
    # Display summary file content
    if os.path.exists(summary_file):
        print("\nSummary file content:")
        with open(summary_file, 'r') as f:
            print(f.read())
    
    # Clean up
    for file in [log_file, summary_file]:
        if os.path.exists(file):
            os.remove(file)
    print(f"✅ Cleaned up files")

# ==============================================================================
# EXERCISE 9: CSV Data Processor
# ==============================================================================

def exercise_9():
    """
    Process employee CSV data.
    """
    import csv
    from collections import defaultdict
    
    # Create sample CSV file
    csv_file = 'employees.csv'
    csv_data = [
        ['Name', 'Department', 'Salary', 'Years'],
        ['Alice', 'Engineering', '75000', '5'],
        ['Bob', 'Marketing', '65000', '3'],
        ['Charlie', 'Engineering', '80000', '7'],
        ['Diana', 'HR', '55000', '2'],
        ['Eve', 'Marketing', '70000', '4']
    ]
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    
    def process_employees(filename):
        """Process employee data from CSV."""
        try:
            employees = []
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert types
                    try:
                        row['Salary'] = float(row['Salary'])
                        row['Years'] = int(row['Years'])
                        employees.append(row)
                    except (ValueError, KeyError) as e:
                        print(f"⚠️ Skipping malformed row: {row} - {e}")
            
            if not employees:
                print("❌ No valid employee data found")
                return
            
            # 1. Average salary by department
            dept_salaries = defaultdict(list)
            for emp in employees:
                dept_salaries[emp['Department']].append(emp['Salary'])
            
            print("\n1. Average Salary by Department:")
            for dept, salaries in dept_salaries.items():
                avg = sum(salaries) / len(salaries)
                print(f"   {dept}: ${avg:,.2f}")
            
            # 2. Employee with highest salary
            highest_paid = max(employees, key=lambda x: x['Salary'])
            print(f"\n2. Highest Paid Employee:")
            print(f"   {highest_paid['Name']} - ${highest_paid['Salary']:,.2f} ({highest_paid['Department']})")
            
            # 3. Total years by department
            dept_years = defaultdict(int)
            for emp in employees:
                dept_years[emp['Department']] += emp['Years']
            
            print(f"\n3. Total Years Experience by Department:")
            for dept, years in dept_years.items():
                print(f"   {dept}: {years} years")
            
            # 4. Add new employee
            new_employee = ['Frank', 'Engineering', '82000', '6']
            with open(filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(new_employee)
            print(f"\n4. Added new employee: {new_employee[0]}")
            
            # Verify addition
            with open(filename, 'r') as f:
                print(f"\nFinal CSV content:")
                for line in f:
                    print(f"   {line.strip()}")
            
        except FileNotFoundError:
            print(f"❌ File '{filename}' not found")
        except Exception as e:
            print(f"❌ Error processing CSV: {e}")
    
    # Process the data
    process_employees(csv_file)
    
    # Clean up
    if os.path.exists(csv_file):
        os.remove(csv_file)
    print(f"\n✅ Cleaned up '{csv_file}'")

# ==============================================================================
# EXERCISE 10: Custom Exception - InsufficientFundsError
# ==============================================================================

def exercise_10():
    """
    Create a BankAccount class with custom exception.
    """
    class InsufficientFundsError(Exception):
        """Raised when account has insufficient funds."""
        def __init__(self, balance, amount):
            self.balance = balance
            self.amount = amount
            self.message = f"Insufficient funds: balance ${balance:.2f}, tried to withdraw ${amount:.2f}"
            super().__init__(self.message)
    
    class NegativeAmountError(Exception):
        """Raised when negative amount is provided."""
        pass
    
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance
            self.transactions = []
        
        def deposit(self, amount):
            """Deposit money into account."""
            if amount < 0:
                raise NegativeAmountError("Cannot deposit negative amount")
            if amount == 0:
                raise ValueError("Deposit amount must be greater than zero")
            
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount:.2f}")
            print(f"  ✅ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        
        def withdraw(self, amount):
            """Withdraw money from account."""
            if amount < 0:
                raise NegativeAmountError("Cannot withdraw negative amount")
            if amount == 0:
                raise ValueError("Withdrawal amount must be greater than zero")
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount:.2f}")
            print(f"  ✅ Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        
        def get_balance(self):
            """Return current balance."""
            return self.balance
        
        def get_transactions(self):
            """Return list of transactions."""
            return self.transactions
    
    # Test the BankAccount class
    print("🏦 Bank Account Test")
    print("-" * 30)
    
    # Create account
    account = BankAccount("Alice", 100)
    print(f"Created account for {account.owner} with balance ${account.balance}")
    
    # Test valid operations
    print("\nTesting valid operations:")
    try:
        account.deposit(50)
        account.withdraw(30)
    except (InsufficientFundsError, NegativeAmountError, ValueError) as e:
        print(f"  ❌ {e}")
    
    # Test insufficient funds
    print("\nTesting insufficient funds:")
    try:
        account.withdraw(200)
    except InsufficientFundsError as e:
        print(f"  ❌ {e}")
    
    # Test negative amounts
    print("\nTesting negative amounts:")
    try:
        account.deposit(-10)
    except NegativeAmountError as e:
        print(f"  ❌ {e}")
    
    try:
        account.withdraw(-5)
    except NegativeAmountError as e:
        print(f"  ❌ {e}")
    
    # Test zero amounts
    print("\nTesting zero amounts:")
    try:
        account.deposit(0)
    except ValueError as e:
        print(f"  ❌ {e}")
    
    # Show transaction history
    print(f"\n📋 Transaction History for {account.owner}:")
    for i, transaction in enumerate(account.get_transactions(), 1):
        print(f"  {i}. {transaction}")
    print(f"  Final balance: ${account.get_balance():.2f}")

# ==============================================================================
# EXERCISE 11: Multi-File Search Tool
# ==============================================================================

def exercise_11():
    """
    Search for text in multiple files.
    """
    import os
    
    # Create test directory and files
    test_dir = 'test_files'
    os.makedirs(test_dir, exist_ok=True)
    
    # Create sample files
    files_content = {
        'file1.txt': "This is file one.\nIt contains some text.\nPython is great!",
        'file2.txt': "File two content.\nMore text here.\nPython programming.",
        'file3.txt': "Third file.\nPython is awesome!\nSearch for Python.",
        'notes.txt': "Personal notes.\nNothing about Python here.",
        'data.csv': "Name,Age,City\nJohn,25,NYC\nJane,30,LA"
    }
    
    for filename, content in files_content.items():
        with open(os.path.join(test_dir, filename), 'w') as f:
            f.write(content)
    
    def search_files(directory, search_term):
        """Search for term in all .txt files in directory."""
        print(f"\n🔍 Searching for '{search_term}' in {directory}")
        print("=" * 50)
        
        try:
            if not os.path.exists(directory):
                raise FileNotFoundError(f"Directory '{directory}' not found")
            
            if not os.path.isdir(directory):
                raise NotADirectoryError(f"'{directory}' is not a directory")
            
            # Get all .txt files
            txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
            
            if not txt_files:
                print("⚠️ No .txt files found in directory")
                return
            
            found_count = 0
            
            for filename in txt_files:
                filepath = os.path.join(directory, filename)
                matches = []
                
                try:
                    with open(filepath, 'r') as f:
                        for line_num, line in enumerate(f, 1):
                            if search_term.lower() in line.lower():
                                matches.append((line_num, line.strip()))
                    
                    if matches:
                        found_count += 1
                        print(f"\n📄 {filename}:")
                        for line_num, line in matches:
                            print(f"   Line {line_num}: {line}")
                
                except PermissionError:
                    print(f"❌ Permission denied: {filename}")
                except Exception as e:
                    print(f"❌ Error reading {filename}: {e}")
            
            if found_count == 0:
                print(f"❌ No matches found for '{search_term}'")
            else:
                print(f"\n✅ Found matches in {found_count} file(s)")
                
        except (FileNotFoundError, NotADirectoryError) as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    # Test the search function
    search_files(test_dir, "python")
    
    print("\n" + "-" * 50)
    search_files(test_dir, "file")
    
    # Test with invalid directory
    print("\n" + "-" * 50)
    search_files("nonexistent_dir", "test")
    
    # Clean up
    import shutil
    shutil.rmtree(test_dir)
    print(f"\n✅ Cleaned up '{test_dir}'")

# ==============================================================================
# EXERCISE 12: File Backup System
# ==============================================================================

def exercise_12():
    """
    Create a file backup system.
    """
    import shutil
    from pathlib import Path
    
    def create_backup(filename):
        """Create backup of a file with versioning."""
        print(f"\n📦 Backing up '{filename}'")
        print("-" * 30)
        
        try:
            # Check if source file exists
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File '{filename}' not found")
            
            # Generate backup filename
            backup_base = f"{filename}.backup"
            backup_file = backup_base
            version = 1
            
            # Check if backup exists and ask user
            while os.path.exists(backup_file):
                print(f"⚠️ Backup file '{backup_file}' already exists")
                choice = input("Choose: [O]verwrite, [N]ew version, [C]ancel: ").lower()
                
                if choice == 'o':
                    # Overwrite existing
                    break
                elif choice == 'n':
                    # Create new version
                    backup_file = f"{filename}.backup.{version}"
                    version += 1
                elif choice == 'c':
                    print("❌ Backup cancelled")
                    return False
                else:
                    print("Invalid choice. Please try again.")
            
            # Create the backup
            shutil.copy2(filename, backup_file)
            print(f"✅ Backup created: '{backup_file}'")
            
            # Show backup info
            source_size = os.path.getsize(filename)
            backup_size = os.path.getsize(backup_file)
            print(f"   Source size: {source_size} bytes")
            print(f"   Backup size: {backup_size} bytes")
            print(f"   Backup verified: {'✅' if source_size == backup_size else '❌'}")
            
            return True
            
        except FileNotFoundError as e:
            print(f"❌ {e}")
        except PermissionError:
            print(f"❌ Permission denied")
        except Exception as e:
            print(f"❌ Backup failed: {e}")
        
        return False
    
    # Test the backup system
    print("🔄 File Backup System")
    
    # Create a test file
    test_file = 'important_data.txt'
    with open(test_file, 'w') as f:
        f.write("This is important data.\nIt needs to be backed up.\n" * 10)
    
    # Test backup
    create_backup(test_file)
    
    # Test backup again (should prompt)
    create_backup(test_file)
    
    # Test with non-existent file
    create_backup('nonexistent.txt')
    
    # Clean up
    for file in os.listdir('.'):
        if file.startswith('important_data.txt') or file.startswith('important_data.txt.backup'):
            os.remove(file)
    print(f"\n✅ Cleaned up test files")

# ==============================================================================
# EXERCISE 13: Data Validation with Exceptions
# ==============================================================================

def exercise_13():
    """
    User registration with custom validation exceptions.
    """
    class ValidationError(Exception):
        """Base validation exception."""
        pass
    
    class UsernameError(ValidationError):
        """Username validation error."""
        pass
    
    class EmailError(ValidationError):
        """Email validation error."""
        pass
    
    class AgeError(ValidationError):
        """Age validation error."""
        pass
    
    class PasswordError(ValidationError):
        """Password validation error."""
        pass
    
    def validate_username(username):
        """Validate username."""
        if len(username) < 3:
            raise UsernameError("Username must be at least 3 characters long")
        if ' ' in username:
            raise UsernameError("Username cannot contain spaces")
        if not username.isalnum():
            raise UsernameError("Username can only contain letters and numbers")
        return True
    
    def validate_email(email):
        """Validate email."""
        if '@' not in email:
            raise EmailError("Email must contain @ symbol")
        if '.' not in email.split('@')[-1]:
            raise EmailError("Email must have a valid domain (e.g., .com)")
        if ' ' in email:
            raise EmailError("Email cannot contain spaces")
        return True
    
    def validate_age(age):
        """Validate age."""
        try:
            age = int(age)
        except ValueError:
            raise AgeError("Age must be a number")
        
        if age < 18:
            raise AgeError("You must be at least 18 years old")
        if age > 120:
            raise AgeError("Please enter a valid age")
        return True
    
    def validate_password(password):
        """Validate password."""
        if len(password) < 8:
            raise PasswordError("Password must be at least 8 characters long")
        if not any(c.isupper() for c in password):
            raise PasswordError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in password):
            raise PasswordError("Password must contain at least one number")
        return True
    
    def register_user():
        """Interactive user registration with validation."""
        print("📝 User Registration")
        print("=" * 40)
        
        user_data = {}
        
        # Get and validate username
        while True:
            try:
                username = input("Username: ").strip()
                validate_username(username)
                user_data['username'] = username
                break
            except UsernameError as e:
                print(f"❌ {e}")
        
        # Get and validate email
        while True:
            try:
                email = input("Email: ").strip()
                validate_email(email)
                user_data['email'] = email
                break
            except EmailError as e:
                print(f"❌ {e}")
        
        # Get and validate age
        while True:
            try:
                age = input("Age: ").strip()
                validate_age(age)
                user_data['age'] = int(age)
                break
            except AgeError as e:
                print(f"❌ {e}")
        
        # Get and validate password
        while True:
            try:
                password = input("Password: ").strip()
                validate_password(password)
                user_data['password'] = '*' * len(password)  # Don't store real password
                break
            except PasswordError as e:
                print(f"❌ {e}")
        
        print("\n✅ Registration successful!")
        print("User data (password hidden):")
        for key, value in user_data.items():
            print(f"  {key}: {value}")
        
        return user_data
    
    # Run registration
    register_user()

# ==============================================================================
# EXERCISE 14: File Organizer
# ==============================================================================

def exercise_14():
    """
    Organize files into folders by extension.
    """
    import shutil
    
    def organize_files(directory):
        """Organize files in directory by extension."""
        print(f"\n📁 Organizing files in '{directory}'")
        print("=" * 40)
        
        try:
            if not os.path.exists(directory):
                raise FileNotFoundError(f"Directory '{directory}' not found")
            
            if not os.path.isdir(directory):
                raise NotADirectoryError(f"'{directory}' is not a directory")
            
            # Get all files in directory
            files = [f for f in os.listdir(directory) 
                    if os.path.isfile(os.path.join(directory, f))]
            
            if not files:
                print("No files to organize")
                return
            
            organized_count = 0
            skipped_count = 0
            
            for filename in files:
                # Skip hidden files and directories
                if filename.startswith('.'):
                    skipped_count += 1
                    continue
                
                # Get file extension
                if '.' in filename:
                    ext = filename.split('.')[-1].lower()
                else:
                    ext = 'no_extension'
                
                # Create folder for extension
                folder_path = os.path.join(directory, ext)
                os.makedirs(folder_path, exist_ok=True)
                
                # Move file
                src = os.path.join(directory, filename)
                dst = os.path.join(folder_path, filename)
                
                try:
                    # Check if destination already exists
                    if os.path.exists(dst):
                        base, ext_file = os.path.splitext(filename)
                        counter = 1
                        while os.path.exists(dst):
                            new_filename = f"{base}_{counter}{ext_file}"
                            dst = os.path.join(folder_path, new_filename)
                            counter += 1
                    
                    shutil.move(src, dst)
                    print(f"  📄 Moved: {filename} -> {ext}/")
                    organized_count += 1
                    
                except PermissionError:
                    print(f"  ❌ Permission denied: {filename}")
                    skipped_count += 1
                except Exception as e:
                    print(f"  ❌ Error moving {filename}: {e}")
                    skipped_count += 1
            
            # Summary
            print(f"\n✅ Organization complete!")
            print(f"   Organized: {organized_count} files")
            print(f"   Skipped: {skipped_count} files")
            
            # Show folders created
            folders = [d for d in os.listdir(directory) 
                      if os.path.isdir(os.path.join(directory, d))]
            print(f"\n📂 Folders created:")
            for folder in folders:
                folder_files = os.listdir(os.path.join(directory, folder))
                print(f"   {folder}/ ({len(folder_files)} files)")
            
        except (FileNotFoundError, NotADirectoryError) as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    # Create test directory with various files
    test_dir = 'test_organize'
    os.makedirs(test_dir, exist_ok=True)
    
    # Create test files
    test_files = [
        'document1.txt', 'document2.txt', 'notes.txt',
        'image1.jpg', 'image2.jpg', 'photo.jpg',
        'script.py', 'main.py', 'utils.py',
        'data.csv', 'report.csv',
        'README.md',
        'config',  # No extension
        '.hidden_file'  # Hidden file
    ]
    
    for filename in test_files:
        with open(os.path.join(test_dir, filename), 'w') as f:
            f.write(f"This is {filename}")
    
    print("Created test files in", test_dir)
    
    # Organize files
    organize_files(test_dir)
    
    # Clean up
    shutil.rmtree(test_dir)
    print(f"\n✅ Cleaned up '{test_dir}'")

# ==============================================================================
# EXERCISE 15: Journal with Exception Logging
# ==============================================================================

def exercise_15():
    """
    Personal journal with exception logging decorator.
    """
    import json
    from datetime import datetime
    from functools import wraps
    
    # Exception logging decorator
    def log_exceptions(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Log the exception
                with open('error.log', 'a') as f:
                    f.write(f"\n{'='*50}\n")
                    f.write(f"Timestamp: {datetime.now()}\n")
                    f.write(f"Function: {func.__name__}\n")
                    f.write(f"Error: {type(e).__name__}: {e}\n")
                    f.write(f"Traceback:\n")
                    traceback.print_exc(file=f)
                
                # Re-raise or handle
                print(f"❌ Error in {func.__name__}: {e}")
                return None
        return wrapper
    
    class Journal:
        def __init__(self, filename='journal.json'):
            self.filename = filename
            self.entries = self.load_entries()
        
        @log_exceptions
        def load_entries(self):
            """Load journal entries from file."""
            if not os.path.exists(self.filename):
                return []
            
            with open(self.filename, 'r') as f:
                return json.load(f)
        
        @log_exceptions
        def save_entries(self):
            """Save journal entries to file."""
            with open(self.filename, 'w') as f:
                json.dump(self.entries, f, indent=2)
        
        @log_exceptions
        def add_entry(self, title, content):
            """Add a new journal entry."""
            entry = {
                'date': datetime.now().isoformat(),
                'title': title,
                'content': content
            }
            self.entries.append(entry)
            self.save_entries()
            print(f"✅ Entry added: {title}")
        
        @log_exceptions
        def view_entries(self):
            """View all journal entries."""
            if not self.entries:
                print("No entries found")
                return
            
            print("\n📔 JOURNAL ENTRIES")
            print("=" * 50)
            for i, entry in enumerate(self.entries, 1):
                date = datetime.fromisoformat(entry['date']).strftime('%Y-%m-%d %H:%M')
                print(f"\n{i}. {entry['title']}")
                print(f"   Date: {date}")
                print(f"   Content: {entry['content'][:100]}...")
        
        @log_exceptions
        def search_entries(self, keyword):
            """Search entries by keyword."""
            keyword = keyword.lower()
            results = []
            
            for entry in self.entries:
                if (keyword in entry['title'].lower() or 
                    keyword in entry['content'].lower()):
                    results.append(entry)
            
            if results:
                print(f"\n🔍 Found {len(results)} entries containing '{keyword}':")
                for entry in results:
                    print(f"  • {entry['title']} ({entry['date'][:10]})")
            else:
                print(f"No entries found containing '{keyword}'")
        
        @log_exceptions
        def delete_entry(self, index):
            """Delete an entry by index."""
            if 0 <= index < len(self.entries):
                deleted = self.entries.pop(index)
                self.save_entries()
                print(f"✅ Deleted: {deleted['title']}")
            else:
                raise IndexError(f"Invalid entry index: {index}")
    
    # Test the journal
    print("📔 Personal Journal")
    print("=" * 40)
    
    journal = Journal()
    
    # Add some entries
    journal.add_entry("First Day", "Started learning about file handling and exceptions in Python.")
    journal.add_entry("Progress Update", "Completed exercises on custom exceptions and file operations.")
    journal.add_entry("Challenges", "Had some trouble with JSON serialization, but figured it out.")
    
    # View entries
    journal.view_entries()
    
    # Search entries
    journal.search_entries("Python")
    journal.search_entries("challenges")
    
    # Test error logging
    print("\nTesting error logging:")
    try:
        journal.delete_entry(10)  # Invalid index
    except IndexError:
        print("Caught expected IndexError")
    
    # Show error log
    if os.path.exists('error.log'):
        print("\n📋 Error Log Content:")
        with open('error.log', 'r') as f:
            print(f.read())
    
    # Clean up
    if os.path.exists(journal.filename):
        os.remove(journal.filename)
    if os.path.exists('error.log'):
        os.remove('error.log')
    print(f"\n✅ Cleaned up journal files")

# ==============================================================================
# MAIN FUNCTION TO RUN ALL SOLUTIONS
# ==============================================================================

def main():
    """
    Run all exercise solutions in sequence.
    """
    print("Module 05: File Handling and Exceptions - Solutions")
    print("=" * 60)
    
    exercises = [
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
        exercise_6, exercise_7, exercise_8, exercise_9, exercise_10,
        exercise_11, exercise_12, exercise_13, exercise_14, exercise_15
    ]
    
    for i, exercise in enumerate(exercises, 1):
        print(f"\nExercise {i}:")
        print("-" * 20)
        exercise()
        
        # Pause between exercises
        if i < len(exercises):
            input("\nPress Enter to continue to next exercise...")

if __name__ == "__main__":
    main()