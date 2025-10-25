#!/usr/bin/env python3
"""
Course Setup Script

This script helps students set up their Python learning environment.
It checks for required tools, creates directory structure, and sets up virtual environment.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Check if Python version is sufficient."""
    version = sys.version_info
    print(f"Python version: {sys.version}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    else:
        print("✅ Python version is compatible")
        return True

def check_pip():
    """Check if pip is available."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, capture_output=True)
        print("✅ pip is available")
        return True
    except subprocess.CalledProcessError:
        print("❌ pip is not available")
        return False

def create_virtual_environment():
    """Create a virtual environment."""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
        
    try:
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def install_requirements():
    """Install required packages."""
    requirements_file = Path("requirements.txt")
    
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
        
    # Determine pip command based on platform
    if platform.system() == "Windows":
        pip_cmd = Path("venv/Scripts/pip.exe")
    else:
        pip_cmd = Path("venv/bin/pip")
    
    try:
        print("Installing requirements...")
        subprocess.run([str(pip_cmd), "install", "-r", "requirements.txt"], check=True)
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def create_course_structure():
    """Create the course directory structure."""
    directories = [
        "exercises/beginner",
        "exercises/intermediate", 
        "exercises/advanced",
        "exercises/solutions",
        "assets/images/diagrams",
        "assets/images/screenshots",
        "assets/cheatsheets",
        "assets/templates/project-template",
        "assets/templates/exercise-template"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created: {directory}")
    
    print("✅ Course structure created")

def display_activation_commands():
    """Display virtual environment activation commands."""
    system = platform.system()
    
    print("\n" + "="*50)
    print("SETUP COMPLETE! 🎉")
    print("="*50)
    
    if system == "Windows":
        print("\nTo activate your virtual environment, run:")
        print("  venv\\Scripts\\activate")
    else:
        print("\nTo activate your virtual environment, run:")
        print("  source venv/bin/activate")
    
    print("\nNext steps:")
    print("1. Activate the virtual environment")
    print("2. Start with Module 00: Getting Started")
    print("3. Happy coding! 🐍")

def main():
    """Main setup function."""
    print("🐍 Python Learning Course Setup")
    print("=" * 40)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
        
    if not check_pip():
        sys.exit(1)
    
    # Setup process
    steps = [
        ("Creating virtual environment", create_virtual_environment),
        ("Installing requirements", install_requirements),
        ("Creating course structure", create_course_structure)
    ]
    
    all_success = True
    for step_name, step_function in steps:
        print(f"\n{step_name}...")
        if not step_function():
            all_success = False
            break
    
    if all_success:
        display_activation_commands()
    else:
        print("\n❌ Setup failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()