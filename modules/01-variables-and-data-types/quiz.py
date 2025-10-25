"""
Module 01: Variables and Data Types - Quiz

Test your knowledge of variables, data types, and basic operations.
Try to answer these questions without looking at the solutions first!
"""

def run_quiz():
    """Run the interactive quiz for Module 01."""
    
    questions = [
        {
            "question": "Which of these is NOT a valid Python variable name?",
            "options": ["my_variable", "2nd_variable", "_private", "variable2"],
            "answer": 1,
            "explanation": "Variable names cannot start with a number."
        },
        {
            "question": "What is the data type of: 3.14",
            "options": ["int", "str", "float", "bool"],
            "answer": 2,
            "explanation": "Numbers with decimal points are float type."
        },
        {
            "question": "What does this code output: print(10 // 3)",
            "options": ["3.333", "3", "3.0", "1"],
            "answer": 1,
            "explanation": "// performs floor division and returns an integer."
        },
        {
            "question": "Which method would you use to remove whitespace from both ends of a string?",
            "options": ["trim()", "clean()", "strip()", "remove_whitespace()"],
            "answer": 2,
            "explanation": "The strip() method removes leading and trailing whitespace."
        },
        {
            "question": "What is the result of: bool('False')",
            "options": ["False", "True", "Error", "None"],
            "answer": 1,
            "explanation": "Any non-empty string is True when converted to boolean."
        },
        {
            "question": "Which operator is used for exponentiation?",
            "options": ["^", "**", "//", "%%"],
            "answer": 1,
            "explanation": "** is the exponentiation operator in Python."
        },
        {
            "question": "What does this code output: print('Hello'[1:4])",
            "options": ["ell", "Hel", "ello", "Hell"],
            "answer": 0,
            "explanation": "String slicing [1:4] gets characters at positions 1, 2, and 3."
        },
        {
            "question": "Which of these converts a string to an integer?",
            "options": ["int()", "str()", "float()", "integer()"],
            "answer": 0,
            "explanation": "int() converts a string to an integer."
        },
        {
            "question": "What is the value of: 5 + 3 * 2",
            "options": ["16", "11", "13", "10"],
            "answer": 1,
            "explanation": "Multiplication has higher precedence than addition."
        },
        {
            "question": "Which string method checks if a string contains only digits?",
            "options": ["isnumeric()", "isdigit()", "isdecimal()", "All of these"],
            "answer": 3,
            "explanation": "All three methods check for digit characters, with slight differences in what they consider valid."
        },
        {
            "question": "What does this code output: print(f'{10:.2f}')",
            "options": ["10", "10.00", "10.0", "10.00%"],
            "answer": 1,
            "explanation": ":.2f formats the number with 2 decimal places."
        },
        {
            "question": "Which of these is a boolean value?",
            "options": ["'True'", "true", "True", "1"],
            "answer": 2,
            "explanation": "Boolean values in Python are True and False (capitalized)."
        },
        {
            "question": "What is the result of: 'Python' + 3",
            "options": ["'Python3'", "'PythonPythonPython'", "Error", "'3Python'"],
            "answer": 2,
            "explanation": "You cannot concatenate a string with an integer directly."
        },
        {
            "question": "Which operator has the highest precedence?",
            "options": ["+ (addition)", "* (multiplication)", "** (exponent)", "= (assignment)"],
            "answer": 2,
            "explanation": "Exponentiation has the highest precedence among these."
        },
        {
            "question": "What does len('Python') return?",
            "options": ["5", "6", "7", "P"],
            "answer": 1,
            "explanation": "len() returns the number of characters in the string."
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Module 01: Variables and Data Types - Quiz")
    print("=" * 50)
    print(f"Answer {total_questions} questions to test your knowledge!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        print("Options:")
        for j, option in enumerate(q['options']):
            print(f"  {j}. {option}")
        
        try:
            user_answer = int(input("Your answer (enter number): "))
            if user_answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer is: {q['answer']}. {q['options'][q['answer']]}")
            
            # Show explanation
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
        print("🎉 Excellent! You have a strong understanding of variables and data types!")
    elif percentage >= 70:
        print("👍 Good job! You understand the core concepts well.")
    elif percentage >= 50:
        print("📚 Not bad! Review the material and you'll improve quickly.")
    else:
        print("💪 Keep practicing! Focus on the fundamental concepts.")
    
    print("\nKey concepts to review:")
    print("• Variable naming rules and conventions")
    print("• Different data types (int, float, str, bool)")
    print("• Type conversion functions (int(), str(), float(), bool())")
    print("• String methods and operations")
    print("• Arithmetic operators and precedence")
    print("• Boolean logic and comparisons")
    print("• String formatting techniques")

if __name__ == "__main__":
    run_quiz()