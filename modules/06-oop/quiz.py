"""
Module 06: Quiz
"""

def run_quiz():
    questions = [
        {
            "question": "What is the special method used to initialize a new object in Python?",
            "options": ["__start__", "__init__", "__create__", "__new__"],
            "answer": 1,
            "explanation": "__init__ is the constructor method in Python classes."
        },
        {
            "question": "What does the 'self' parameter represent in a method?",
            "options": ["The class itself", "Global variables", "The specific instance of the object", "The parent class"],
            "answer": 2,
            "explanation": "'self' refers to the instance calling the method, allowing access to its attributes."
        },
        {
            "question": "What is Inheritance?",
            "options": ["Hiding data inside a class", "Creating a new class from an existing class", "Running a class twice", "Importing a module"],
            "answer": 1,
            "explanation": "Inheritance allows a class (child) to derive attributes and methods from another class (parent)."
        },
        {
            "question": "How do you access an attribute `name` of an object `obj`?",
            "options": ["obj->name", "obj[name]", "obj.name", "name(obj)"],
            "answer": 2,
            "explanation": "Dot notation (object.attribute) is used to access members."
        }
    ]
    
    score = 0
    print("Module 06 Quiz: Object-Oriented Programming\n" + "="*40)
    
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
