"""
Module 04: Data Structures - Quiz

Test your knowledge of lists, tuples, dictionaries, and sets.
Try to answer these questions without looking at the solutions first!
"""

def run_quiz():
    """Run the interactive quiz for Module 04."""
    
    questions = [
        {
            "question": "Which of the following is mutable?",
            "options": ["tuple", "string", "list", "integer"],
            "answer": 2,
            "explanation": "Lists are mutable (can be changed). Tuples, strings, and integers are immutable."
        },
        {
            "question": "What does this code output: fruits = ['apple', 'banana', 'orange']; print(fruits[-1])",
            "options": ["apple", "banana", "orange", "Error"],
            "answer": 2,
            "explanation": "Index -1 refers to the last element in the list."
        },
        {
            "question": "How do you create an empty set?",
            "options": ["set()", "{}", "[]", "()"],
            "answer": 0,
            "explanation": "set() creates an empty set. {} creates an empty dictionary."
        },
        {
            "question": "What is the result of: {1, 2, 3} & {2, 3, 4}",
            "options": ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "Error"],
            "answer": 1,
            "explanation": "The & operator returns the intersection of two sets."
        },
        {
            "question": "Which method adds an element to a set?",
            "options": ["append()", "add()", "insert()", "push()"],
            "answer": 1,
            "explanation": "add() is used for sets. append() and insert() are for lists."
        },
        {
            "question": "What does this code return: {'a': 1, 'b': 2}.get('c', 0)",
            "options": ["None", "KeyError", "0", "False"],
            "answer": 2,
            "explanation": "get() returns the default value (0) when the key doesn't exist."
        },
        {
            "question": "Which of these can be used as a dictionary key?",
            "options": ["list", "dictionary", "tuple", "set"],
            "answer": 2,
            "explanation": "Dictionary keys must be immutable. Tuples are immutable, so they can be keys."
        },
        {
            "question": "What is the result of: (1, 2, 3) + (4, 5)",
            "options": ["(1, 2, 3, 4, 5)", "[1, 2, 3, 4, 5]", "Error", "(5, 7, 8)"],
            "answer": 0,
            "explanation": "Tuples support concatenation with the + operator."
        },
        {
            "question": "How do you create a list of squares for numbers 1-5 using list comprehension?",
            "options": ["[x**2 for x in range(5)]", "[x**2 for x in range(1, 6)]", "map(x**2, range(1,6))", "list(x**2, range(1,6))"],
            "answer": 1,
            "explanation": "[x**2 for x in range(1, 6)] creates squares of 1 through 5."
        },
        {
            "question": "What does this code output: ' '.join(['Hello', 'World'])",
            "options": ["HelloWorld", "Hello World", "['Hello', 'World']", "Error"],
            "answer": 1,
            "explanation": "join() concatenates list elements with the string as separator."
        },
        {
            "question": "Which statement about tuples is FALSE?",
            "options": [
                "Tuples are ordered",
                "Tuples are immutable",
                "Tuples can contain mixed data types",
                "Tuples can be modified after creation"
            ],
            "answer": 3,
            "explanation": "Tuples cannot be modified after creation - they are immutable."
        },
        {
            "question": "What is the result of: len([1, [2, 3], 4])",
            "options": ["3", "4", "2", "Error"],
            "answer": 0,
            "explanation": "len() counts the top-level elements. The nested list counts as one element."
        },
        {
            "question": "How do you remove the last item from a list and return it?",
            "options": ["remove()", "delete()", "pop()", "discard()"],
            "answer": 2,
            "explanation": "pop() removes and returns the last item by default."
        },
        {
            "question": "What is the result of: set([1, 2, 2, 3, 3, 3])",
            "options": ["[1, 2, 2, 3, 3, 3]", "{1, 2, 3}", "Error", "(1, 2, 3)"],
            "answer": 1,
            "explanation": "Sets automatically remove duplicates, so result is {1, 2, 3}."
        },
        {
            "question": "Which dictionary method returns all key-value pairs as tuples?",
            "options": ["keys()", "values()", "items()", "pairs()"],
            "answer": 2,
            "explanation": "items() returns a view of key-value pairs as tuples."
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print("Module 04: Data Structures - Quiz")
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
        print("🎉 Excellent! You have a strong understanding of data structures!")
    elif percentage >= 70:
        print("👍 Good job! You understand the core concepts well.")
    elif percentage >= 50:
        print("📚 Not bad! Review the material and you'll improve quickly.")
    else:
        print("💪 Keep practicing! Focus on understanding each data structure's properties.")
    
    print("\nKey concepts to review:")
    print("• List operations and methods")
    print("• Tuple immutability and unpacking")
    print("• Dictionary key-value pairs and methods")
    print("• Set operations and uniqueness")
    print("• When to use each data structure")
    print("• List comprehensions for concise code")
    print("• Nested data structures")

if __name__ == "__main__":
    run_quiz()