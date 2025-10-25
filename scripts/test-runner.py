#!/usr/bin/env python3
"""
Automated Exercise Test Runner

This script runs tests on exercise solutions to verify they work correctly.
It can be used by students to check their work or by instructors to validate solutions.
"""

import importlib.util
import sys
import os
from pathlib import Path
import unittest
import tempfile
import io
from contextlib import redirect_stdout, redirect_stderr

class ExerciseTester:
    """Test runner for Python exercises."""
    
    def __init__(self):
        self.results = {}
        
    def load_module(self, file_path):
        """Dynamically load a Python module from file path."""
        try:
            module_name = Path(file_path).stem
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            print(f"❌ Failed to load {file_path}: {e}")
            return None
    
    def test_basic_syntax(self, file_path):
        """Test basic Python syntax by attempting to import the module."""
        try:
            module = self.load_module(file_path)
            if module is not None:
                return True, "Syntax is valid"
            else:
                return False, "Syntax errors found"
        except SyntaxError as e:
            return False, f"Syntax error: {e}"
    
    def test_function_exists(self, file_path, function_name):
        """Test if a specific function exists in the module."""
        module = self.load_module(file_path)
        if module is None:
            return False, f"Could not load module"
            
        if hasattr(module, function_name):
            return True, f"Function '{function_name}' exists"
        else:
            return False, f"Function '{function_name}' not found"
    
    def test_function_output(self, file_path, function_name, test_input, expected_output):
        """Test if a function produces expected output for given input."""
        module = self.load_module(file_path)
        if module is None:
            return False, "Could not load module"
            
        if not hasattr(module, function_name):
            return False, f"Function '{function_name}' not found"
            
        func = getattr(module, function_name)
        
        try:
            # Capture output
            output_capture = io.StringIO()
            with redirect_stdout(output_capture):
                if test_input is not None:
                    result = func(*test_input)
                else:
                    result = func()
            
            output = output_capture.getvalue().strip()
            
            # Check if function returns value or prints output
            if expected_output is not None:
                if result == expected_output:
                    return True, f"Function returned correct value: {result}"
                else:
                    return False, f"Expected {expected_output}, got {result}"
            elif output:
                return True, f"Function printed output: {output}"
            else:
                return True, "Function executed successfully"
                
        except Exception as e:
            return False, f"Function execution failed: {e}"
    
    def run_exercise_tests(self, exercise_file, test_cases):
        """Run a series of tests on an exercise file."""
        print(f"\n🧪 Testing {exercise_file}")
        print("-" * 40)
        
        all_passed = True
        results = []
        
        for i, test_case in enumerate(test_cases, 1):
            test_type = test_case['type']
            print(f"Test {i}: {test_case['description']}")
            
            if test_type == 'syntax':
                passed, message = self.test_basic_syntax(exercise_file)
            elif test_type == 'function_exists':
                passed, message = self.test_function_exists(exercise_file, test_case['function'])
            elif test_type == 'function_output':
                passed, message = self.test_function_output(
                    exercise_file, 
                    test_case['function'],
                    test_case.get('input'),
                    test_case.get('expected_output')
                )
            else:
                passed, message = False, f"Unknown test type: {test_type}"
            
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"  {status}: {message}")
            
            results.append({
                'test': test_case['description'],
                'passed': passed,
                'message': message
            })
            
            if not passed:
                all_passed = False
        
        return all_passed, results

def main():
    """Main function to run exercise tests."""
    if len(sys.argv) < 2:
        print("Usage: python test-runner.py <exercise_file.py>")
        sys.exit(1)
    
    exercise_file = sys.argv[1]
    
    if not os.path.exists(exercise_file):
        print(f"❌ Exercise file not found: {exercise_file}")
        sys.exit(1)
    
    # Example test cases - these would be customized per exercise
    test_cases = [
        {
            'type': 'syntax',
            'description': 'Basic syntax validation'
        },
        {
            'type': 'function_exists', 
            'description': 'Check main function exists',
            'function': 'main'
        }
    ]
    
    tester = ExerciseTester()
    all_passed, results = tester.run_exercise_tests(exercise_file, test_cases)
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 All tests passed! Exercise completed successfully.")
    else:
        print("❌ Some tests failed. Please review your code.")
        sys.exit(1)

if __name__ == "__main__":
    main()