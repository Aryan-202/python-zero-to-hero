"""
Module 03: Functions and Modules - Quiz
"""

def run_quiz():
    """Run the interactive quiz for Module 03."""
    
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "func", "define"],
            "answer": 1,
            "explanation": "Functions are defined using the 'def' keyword."
        },
        {
            "question": "What is the output of: def foo(x=5): return x; print(foo())",
            "options": ["Error", "None", "5", "0"],
            "answer": 2,
            "explanation": "The function uses the default argument 5 when no argument is passed."
        },
        {
            "question": "Variables defined inside a function are called:",
            "options": ["Global variables", "Local variables", "Static variables", "Class variables"],
            "answer": 1,
            "explanation": "Variables created inside a function are local to that function's scope."
        },
        {
            "question": "Which statement is used to send a value back from a function?",
            "options": ["send", "output", "return", "back"],
            "answer": 2,
            "explanation": "'return' sends the result back to the caller."
        },
        {
            "question": "What is a lambda function?",
            "options": ["A function that loops forever", "A built-in math function", "An anonymous single-line function", "A function with no arguments"],
            "answer": 2,
            "explanation": "Lambda functions are small, anonymous functions defined with the 'lambda' keyword."
        },
        {
            "question": "How do you import a specific function `sqrt` from the `math` module?",
            "options": ["import math.sqrt", "from math import sqrt", "using math.sqrt", "include math"],
            "answer": 1,
            "explanation": "Use 'from module import function' syntax."
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Module 03: Functions and Modules - Quiz")
    print("=" * 50)
    print(f"Answer {total_questions} questions!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        print("Options:")
        for j, option in enumerate(q['options']):
            print(f"  {j}. {option}")
        
        try:
            user_answer = input("Your answer (enter number): ")
            if not user_answer.isdigit():
                 print(f"❌ Invalid input.")
                 continue
                 
            user_answer = int(user_answer)
            
            if user_answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer is: {q['answer']}. {q['options'][q['answer']]}")
            
            print(f"💡 Explanation: {q['explanation']}\n")
            
        except (ValueError, IndexError):
            print(f"❌ Invalid input.")
            print(f"💡 Explanation: {q['explanation']}\n")
    
    percentage = (score / total_questions) * 100
    print(f"Your score: {score}/{total_questions} ({percentage:.1f}%)")

if __name__ == "__main__":
    run_quiz()
