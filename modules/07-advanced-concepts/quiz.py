"""
Module 07: Quiz
"""

def run_quiz():
    questions = [
        {
            "question": "What is the output of: [x*2 for x in [1, 2, 3]]",
            "options": ["[1, 2, 3]", "[2, 4, 6]", "[1, 4, 9]", "Error"],
            "answer": 1,
            "explanation": "It doubles each element in the list."
        },
        {
            "question": "Which keyword creates an anonymous function?",
            "options": ["def", "func", "lambda", "anon"],
            "answer": 2,
            "explanation": "Lambda functions are created using the 'lambda' keyword."
        },
        {
            "question": "What is a decorator used for?",
            "options": ["To paint the IDE", "To modify or extend the behavior of a function/class", "To declare a variable", "To delete a file"],
            "answer": 1,
            "explanation": "Decorators wrap another function to extend its behavior without modifying its source code."
        },
        {
            "question": "Which syntax applies a decorator called 'my_dec'?",
            "options": ["#my_dec", "@my_dec", "$my_dec", "&my_dec"],
            "answer": 1,
            "explanation": "The @ symbol is used for syntactic sugar to apply decorators."
        }
    ]
    
    score = 0
    print("Module 07 Quiz: Advanced Concepts\n" + "="*40)
    
    for i, q in enumerate(questions, 1):
        print(f"\n{i}. {q['question']}")
        for j, opt in enumerate(q['options']):
            print(f"  {j}. {opt}")
        
        try:
            ans = int(input("Answer: "))
            if ans == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. Answer: {q['options'][q['answer']]}")
        except:
            print(f"❌ Invalid. Answer: {q['options'][q['answer']]}")
        print(f"💡 {q['explanation']}")
            
    print(f"\nScore: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
