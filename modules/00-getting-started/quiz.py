"""
Module 00: Getting Started - Quiz

Test your knowledge of the concepts covered in this module.
Try to answer these questions without looking at the solutions first!
"""

def run_quiz():
    """Run the interactive quiz for Module 00."""
    
    questions = [
        {
            "question": "What symbol is used for single-line comments in Python?",
            "options": ["//", "#", "--", "/*"],
            "answer": 1
        },
        {
            "question": "Which of these is NOT a valid Python variable name?",
            "options": ["my_variable", "2nd_variable", "_private", "variable2"],
            "answer": 1
        },
        {
            "question": "What does the ** operator do in Python?",
            "options": [
                "Multiplication",
                "Exponentiation (power)",
                "String repetition", 
                "Comment"
            ],
            "answer": 1
        },
        {
            "question": "Which function is used to get input from the user?",
            "options": ["input()", "get()", "read()", "scan()"],
            "answer": 0
        },
        {
            "question": "What is the result of: print(10 / 3)",
            "options": ["3", "3.333...", "3.0", "Error"],
            "answer": 1
        },
        {
            "question": "Which of these is a boolean value in Python?",
            "options": ["'True'", "true", "True", "1"],
            "answer": 2
        },
        {
            "question": "What does len('Python') return?",
            "options": ["5", "6", "7", "P"],
            "answer": 1
        },
        {
            "question": "How do you convert 25.7 to an integer?",
            "options": ["int(25.7)", "integer(25.7)", "to_int(25.7)", "25.7.int()"],
            "answer": 0
        },
        {
            "question": "What is the output of: print('Hello' + 'World')",
            "options": ["HelloWorld", "Hello World", "Hello+World", "Error"],
            "answer": 0
        },
        {
            "question": "Which of these is used for multi-line strings and comments?",
            "options": ["'''triple quotes'''", "// comments", "/* comments */", "-- comments"],
            "answer": 0
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Module 00: Getting Started - Quiz")
    print("=" * 40)
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
        except (ValueError, IndexError):
            print(f"❌ Invalid input. The correct answer is: {q['answer']}. {q['options'][q['answer']]}")
        
        print()  # Empty line for readability
    
    # Calculate percentage
    percentage = (score / total_questions) * 100
    
    print("Quiz Complete!")
    print("=" * 20)
    print(f"Your score: {score}/{total_questions} ({percentage:.1f}%)")
    
    # Provide feedback based on score
    if percentage >= 90:
        print("🎉 Excellent! You've mastered the basics!")
    elif percentage >= 70:
        print("👍 Good job! You have a solid understanding.")
    elif percentage >= 50:
        print("📚 Not bad! Review the material and try again.")
    else:
        print("💪 Keep practicing! Review the module and retake the quiz.")
    
    print("\nKey concepts to review:")
    print("• Python syntax and comments")
    print("• Variables and data types") 
    print("• Basic operations and functions")
    print("• String manipulation")
    print("• Type conversion")

if __name__ == "__main__":
    run_quiz()