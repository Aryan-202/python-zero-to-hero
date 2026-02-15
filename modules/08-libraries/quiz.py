"""
Module 08: Quiz
"""

def run_quiz():
    questions = [
        {
            "question": "What is the name of the package installer for Python?",
            "options": ["npm", "gem", "pip", "brew"],
            "answer": 2,
            "explanation": "pip is the standard package installer for Python."
        },
        {
            "question": "Which command installs a package named 'requests'?",
            "options": ["pip add requests", "pip install requests", "python install requests", "pip get requests"],
            "answer": 1,
            "explanation": "'pip install <package>' is the command."
        },
        {
            "question": "What is a virtual environment used for?",
            "options": ["To run Python faster", "To isolate project dependencies", "To run Python in the cloud", "To debug code"],
            "answer": 1,
            "explanation": "Virtual environments allow different projects to have different versions of libraries without conflict."
        },
        {
            "question": "How do you rename a module when importing it?",
            "options": ["import pandas as pd", "import pandas rename pd", "using pandas as pd", "rename pandas to pd"],
            "answer": 0,
            "explanation": "The 'as' keyword allows aliasing imports."
        }
    ]
    
    score = 0
    print("Module 08 Quiz: External Libraries\n" + "="*40)
    
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
