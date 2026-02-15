"""
Module 02: Control Flow - Quiz

Test your knowledge of conditional statements and loops.
Try to answer these questions without looking at the solutions first!
"""

def run_quiz():
    """Run the interactive quiz for Module 02."""
    
    questions = [
        {
            "question": "Which keyword is used for 'else if' in Python?",
            "options": ["elseif", "else if", "elif", "case"],
            "answer": 2,
            "explanation": "Python uses 'elif' as the keyword for else-if conditions."
        },
        {
            "question": "What is the output of range(3)?",
            "options": ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "1, 2"],
            "answer": 1,
            "explanation": "range(n) generates numbers from 0 up to n-1."
        },
        {
            "question": "Which statement stops a loop immediately?",
            "options": ["stop", "exit", "continue", "break"],
            "answer": 3,
            "explanation": "'break' terminates the loop entirely."
        },
        {
            "question": "What does 'continue' do in a loop?",
            "options": ["Restarts the loop", "Exits the program", "Skips the rest of the current iteration", "Pauses execution"],
            "answer": 2,
            "explanation": "'continue' skips the remaining code in the current iteration and moves to the next one."
        },
        {
            "question": "How many times will this loop run? `for i in range(2, 6):`",
            "options": ["3 times", "4 times", "5 times", "6 times"],
            "answer": 1,
            "explanation": "It runs for 2, 3, 4, 5. That's 4 iterations."
        },
        {
            "question": "Which logical operator returns True only if BOTH operands are True?",
            "options": ["or", "not", "and", "xor"],
            "answer": 2,
            "explanation": "'and' requires both conditions to be True."
        },
        {
            "question": "What happens if a while loop condition never becomes False?",
            "options": ["It stops automatically", "It runs once", "It creates an infinite loop", "It raises an error"],
            "answer": 2,
            "explanation": "If the condition is always True, the loop runs forever (infinite loop)."
        },
        {
            "question": "Can you nest an if statement inside a for loop?",
            "options": ["Yes", "No", "Only in functions", "Only in while loops"],
            "answer": 0,
            "explanation": "Yes, you can nest any control structure inside any other."
        },
        {
            "question": "What is the correct syntax for a while loop?",
            "options": ["while x > 5 {}", "while (x > 5)", "while x > 5:", "loop x > 5:"],
            "answer": 2,
            "explanation": "Python uses 'while condition:' syntax, without parentheses or braces."
        },
        {
            "question": "What does range(1, 10, 2) produce?",
            "options": ["1, 2, 3...", "1, 3, 5, 7, 9", "2, 4, 6, 8", "1, 10"],
            "answer": 1,
            "explanation": "Start at 1, stop before 10, step by 2: 1, 3, 5, 7, 9."
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Module 02: Control Flow - Quiz")
    print("=" * 50)
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
    
    if percentage >= 70:
        print("🎉 Great job!")
    else:
        print("💪 Keep practicing coverage!")

if __name__ == "__main__":
    run_quiz()
