"""
Module 05: Quiz
"""

def run_quiz():
    questions = [
        {
            "question": "Which mode should you use to open a file for writing (overwriting existing content)?",
            "options": ["'r'", "'w'", "'a'", "'x'"],
            "answer": 1,
            "explanation": "'w' opens for writing, truncating the file first. 'a' is for appending."
        },
        {
            "question": "What is the best way to open a file to ensure it closes automatically?",
            "options": ["file.open()", "open(file, close=True)", "using a 'with' statement", "try: file.open()"],
            "answer": 2,
            "explanation": "The 'with' statement (context manager) automatically closes the file even if errors occur."
        },
        {
            "question": "Which exception is raised when you try to open a file that doesn't exist (in read mode)?",
            "options": ["IOError", "TypeError", "ValueError", "FileNotFoundError"],
            "answer": 3,
            "explanation": "FileNotFoundError is raised specifically when a file cannot be found."
        },
        {
            "question": "What does the 'finally' block do in a try-except structure?",
            "options": ["Runs only if no error occurs", "Runs only if an error occurs", "Runs always, regardless of errors", "Stops the program"],
            "answer": 2,
            "explanation": "'finally' creates a block of code that allows you to execute code regardless of the result of the try- and except blocks."
        }
    ]
    
    score = 0
    print("Module 05 Quiz: File Handling & Exceptions\n" + "="*40)
    
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
