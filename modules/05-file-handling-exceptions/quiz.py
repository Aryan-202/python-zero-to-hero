"""
Module 05: File Handling and Exceptions - Quiz

Test your knowledge of file operations and exception handling.
"""

def run_quiz():
    """Run the interactive quiz for Module 05."""
    
    questions = [
        {
            "question": "Which mode opens a file for writing only, creating a new file or truncating existing?",
            "options": ["'r'", "'a'", "'w'", "'x'"],
            "answer": 2,
            "explanation": "'w' mode opens for writing, creating or truncating the file."
        },
        {
            "question": "What does the 'with' statement do when working with files?",
            "options": [
                "Prevents file corruption",
                "Automatically closes the file",
                "Encrypts the file",
                "Makes files read-only"
            ],
            "answer": 1,
            "explanation": "The with statement ensures the file is properly closed after the block executes."
        },
        {
            "question": "Which exception is raised when trying to open a file that doesn't exist?",
            "options": ["IOError", "FileNotFoundError", "OSError", "FileError"],
            "answer": 1,
            "explanation": "FileNotFoundError is raised when the file doesn't exist."
        },
        {
            "question": "What happens in a try-except block if no exception occurs?",
            "options": [
                "The except block executes",
                "The else block executes",
                "The finally block is skipped",
                "Nothing happens"
            ],
            "answer": 1,
            "explanation": "The else block executes only if no exception occurs in the try block."
        },
        {
            "question": "Which method reads all lines from a file into a list?",
            "options": ["read()", "readline()", "readlines()", "getlines()"],
            "answer": 2,
            "explanation": "readlines() reads all lines and returns them as a list."
        },
        {
            "question": "What is the purpose of the finally block?",
            "options": [
                "To handle exceptions",
                "To execute code regardless of whether an exception occurred",
                "To catch specific exceptions",
                "To raise exceptions"
            ],
            "answer": 1,
            "explanation": "The finally block always executes, whether an exception occurred or not."
        },
        {
            "question": "Which statement is used to raise an exception manually?",
            "options": ["throw", "raise", "except", "error"],
            "answer": 1,
            "explanation": "The 'raise' statement is used to raise exceptions manually."
        },
        {
            "question": "What does the 'a' mode do when opening a file?",
            "options": [
                "Appends to the end of the file",
                "Writes at the beginning",
                "Reads the file",
                "Archives the file"
            ],
            "answer": 0,
            "explanation": "'a' (append) mode opens the file for writing at the end."
        },
        {
            "question": "Which of these is NOT a built-in exception in Python?",
            "options": ["ValueError", "TypeError", "SyntaxError", "FileException"],
            "answer": 3,
            "explanation": "FileException is not a built-in exception. FileNotFoundError is the correct one."
        },
        {
            "question": "What happens if you open a file in 'x' mode and it already exists?",
            "options": [
                "It overwrites the file",
                "It appends to the file",
                "It raises FileExistsError",
                "It opens in read mode"
            ],
            "answer": 2,
            "explanation": "'x' mode is exclusive creation - it fails if the file already exists."
        },
        {
            "question": "How do you create a custom exception?",
            "options": [
                "Define a function",
                "Create a class inheriting from Exception",
                "Use the 'exception' keyword",
                "It's not possible"
            ],
            "answer": 1,
            "explanation": "Custom exceptions are created by defining a class that inherits from Exception."
        },
        {
            "question": "What does the 'seek()' method do?",
            "options": [
                "Searches for text in file",
                "Moves the file pointer to a specific position",
                "Deletes file content",
                "Renames the file"
            ],
            "answer": 1,
            "explanation": "seek() moves the file pointer to a specified position in the file."
        },
        {
            "question": "Which block is optional in a try-except statement?",
            "options": ["try", "except", "finally", "All are required"],
            "answer": 2,
            "explanation": "finally is optional. You must have at least one except block."
        },
        {
            "question": "What happens when you catch an exception but don't handle it?",
            "options": [
                "The program continues normally",
                "The exception is ignored",
                "It's bad practice and can hide bugs",
                "Python automatically handles it"
            ],
            "answer": 2,
            "explanation": "Catching exceptions without handling them is bad practice - it hides errors."
        },
        {
            "question": "Which method writes a list of lines to a file?",
            "options": ["write()", "writelines()", "writelist()", "writeall()"],
            "answer": 1,
            "explanation": "writelines() writes a list of lines to the file (without adding newlines)."
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Module 05: File Handling and Exceptions - Quiz")
    print("=" * 60)
    print(f"Answer {total_questions} questions to test your knowledge!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        print("Options:")
        for j, option in enumerate(q['options']):
            print(f"  {j}. {option}")
        
        try:
            user_answer = input("Your answer (enter number): ")
            if not user_answer.isdigit():
                print(f"❌ Invalid input. Please enter a number.")
                print(f"The correct answer is: {q['answer']}. {q['options'][q['answer']]}")
                print(f"💡 Explanation: {q['explanation']}\n")
                continue
                
            user_answer = int(user_answer)
            
            if user_answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer is: {q['answer']}. {q['options'][q['answer']]}")
            
            print(f"💡 Explanation: {q['explanation']}")
            
        except (ValueError, IndexError):
            print(f"❌ Invalid input. The correct answer is: {q['answer']}. {q['options'][q['answer']]}")
            print(f"💡 Explanation: {q['explanation']}")
        
        print()  # Empty line for readability
    
    # Calculate percentage
    percentage = (score / total_questions) * 100
    
    print("Quiz Complete!")
    print("=" * 20)
    print(f"Your score: {score}/{total_questions} ({percentage:.1f}%)")
    
    # Provide feedback based on score
    if percentage >= 90:
        print("🎉 Excellent! You have a strong understanding of file handling and exceptions!")
    elif percentage >= 70:
        print("👍 Good job! You understand the core concepts well.")
    elif percentage >= 50:
        print("📚 Not bad! Review the material and you'll improve quickly.")
    else:
        print("💪 Keep practicing! Focus on understanding file modes and exception handling flow.")
    
    print("\nKey concepts to review:")
    print("• File modes (r, w, a, x, b, t, +)")
    print("• Context managers (with statement)")
    print("• try/except/else/finally blocks")
    print("• Common built-in exceptions")
    print("• Raising exceptions manually")
    print("• Creating custom exceptions")
    print("• Best practices for error handling")

if __name__ == "__main__":
    run_quiz()