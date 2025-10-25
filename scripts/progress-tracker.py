#!/usr/bin/env python3
"""
Student Progress Tracker

This script helps students track their progress through the Python course.
It maintains a progress file and provides statistics and recommendations.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
import argparse

class ProgressTracker:
    """Track and manage student learning progress."""
    
    def __init__(self, progress_file=".learning_progress.json"):
        self.progress_file = Path(progress_file)
        self.progress = self.load_progress()
    
    def load_progress(self):
        """Load progress from file or create new progress structure."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        else:
            return {
                "student_info": {
                    "start_date": datetime.now().isoformat(),
                    "last_activity": datetime.now().isoformat()
                },
                "modules": {},
                "exercises_completed": 0,
                "projects_completed": 0,
                "quizzes_taken": 0,
                "streak": 0,
                "total_study_time": 0
            }
    
    def save_progress(self):
        """Save progress to file."""
        self.progress["student_info"]["last_activity"] = datetime.now().isoformat()
        
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def start_module(self, module_name):
        """Mark a module as started."""
        if module_name not in self.progress["modules"]:
            self.progress["modules"][module_name] = {
                "started": datetime.now().isoformat(),
                "completed": False,
                "exercises_completed": 0,
                "total_exercises": 10,  # This would be dynamic in real implementation
                "time_spent": 0,
                "quiz_score": None
            }
        self.save_progress()
        print(f"🎯 Started module: {module_name}")
    
    def complete_exercise(self, module_name, exercise_name):
        """Mark an exercise as completed."""
        if module_name not in self.progress["modules"]:
            self.start_module(module_name)
        
        module = self.progress["modules"][module_name]
        module["exercises_completed"] += 1
        self.progress["exercises_completed"] += 1
        
        # Update streak
        self.update_streak()
        
        self.save_progress()
        print(f"✅ Completed exercise: {exercise_name}")
    
    def complete_module(self, module_name, quiz_score=None):
        """Mark a module as completed."""
        if module_name in self.progress["modules"]:
            module = self.progress["modules"][module_name]
            module["completed"] = True
            module["completed_date"] = datetime.now().isoformat()
            if quiz_score is not None:
                module["quiz_score"] = quiz_score
                self.progress["quizzes_taken"] += 1
            
            self.save_progress()
            print(f"🎉 Completed module: {module_name}")
        else:
            print(f"Module {module_name} not found in progress")
    
    def complete_project(self, project_name):
        """Mark a project as completed."""
        self.progress["projects_completed"] += 1
        self.update_streak()
        self.save_progress()
        print(f"🚀 Completed project: {project_name}")
    
    def update_streak(self):
        """Update learning streak based on recent activity."""
        last_activity = datetime.fromisoformat(self.progress["student_info"]["last_activity"])
        current_time = datetime.now()
        
        # If activity was yesterday or today, increment streak
        if current_time.date() == last_activity.date():
            # Same day, don't change streak
            pass
        elif current_time.date() == (last_activity.date() + timedelta(days=1)):
            # Consecutive day
            self.progress["streak"] += 1
        else:
            # Broken streak
            self.progress["streak"] = 1
    
    def add_study_time(self, minutes):
        """Add study time to total."""
        self.progress["total_study_time"] += minutes
        self.save_progress()
        print(f"⏰ Added {minutes} minutes of study time")
    
    def get_progress_stats(self):
        """Calculate and return progress statistics."""
        total_modules = 15  # Total modules in the course
        completed_modules = sum(1 for m in self.progress["modules"].values() if m["completed"])
        
        total_exercises = sum(m["exercises_completed"] for m in self.progress["modules"].values())
        
        return {
            "modules_completed": completed_modules,
            "modules_total": total_modules,
            "module_progress": (completed_modules / total_modules) * 100,
            "exercises_completed": total_exercises,
            "projects_completed": self.progress["projects_completed"],
            "quizzes_taken": self.progress["quizzes_taken"],
            "current_streak": self.progress["streak"],
            "total_study_hours": self.progress["total_study_time"] / 60
        }
    
    def show_progress(self):
        """Display progress overview."""
        stats = self.get_progress_stats()
        
        print("\n" + "="*50)
        print("📊 YOUR LEARNING PROGRESS")
        print("="*50)
        
        print(f"🎯 Modules Completed: {stats['modules_completed']}/{stats['modules_total']} "
              f"({stats['module_progress']:.1f}%)")
        print(f"✅ Exercises Completed: {stats['exercises_completed']}")
        print(f"🚀 Projects Completed: {stats['projects_completed']}")
        print(f"📝 Quizzes Taken: {stats['quizzes_taken']}")
        print(f"🔥 Current Streak: {stats['current_streak']} days")
        print(f"⏰ Total Study Time: {stats['total_study_hours']:.1f} hours")
        
        # Show module-specific progress
        print(f"\n📚 Module Progress:")
        for module_name, module_data in self.progress["modules"].items():
            status = "✅" if module_data["completed"] else "🔄"
            exercises = f"{module_data['exercises_completed']}/{module_data['total_exercises']}"
            print(f"  {status} {module_name}: {exercises} exercises")
        
        # Recommendations
        print(f"\n💡 Recommendations:")
        if stats['module_progress'] < 25:
            print("  • Focus on completing the foundational modules")
        elif stats['module_progress'] < 50:
            print("  • Great start! Continue with intermediate concepts")
        elif stats['module_progress'] < 75:
            print("  • You're doing well! Tackle some projects")
        else:
            print("  • Almost there! Complete the final modules and projects")
        
        if stats['current_streak'] < 3:
            print("  • Try to code every day to build a streak!")
        elif stats['current_streak'] < 7:
            print("  • Good streak! Keep going!")
        else:
            print("  • Amazing streak! You're building great habits!")

def main():
    """Main function for progress tracking."""
    parser = argparse.ArgumentParser(description="Track your Python learning progress")
    parser.add_argument("--show", action="store_true", help="Show current progress")
    parser.add_argument("--start-module", help="Start a new module")
    parser.add_argument("--complete-exercise", nargs=2, 
                       metavar=("MODULE", "EXERCISE"), 
                       help="Mark an exercise as completed")
    parser.add_argument("--complete-module", help="Mark a module as completed")
    parser.add_argument("--complete-project", help="Mark a project as completed")
    parser.add_argument("--study-time", type=int, help="Add study time in minutes")
    
    args = parser.parse_args()
    
    tracker = ProgressTracker()
    
    if args.start_module:
        tracker.start_module(args.start_module)
    elif args.complete_exercise:
        module, exercise = args.complete_exercise
        tracker.complete_exercise(module, exercise)
    elif args.complete_module:
        tracker.complete_module(args.complete_module)
    elif args.complete_project:
        tracker.complete_project(args.complete_project)
    elif args.study_time:
        tracker.add_study_time(args.study_time)
    
    # Always show progress if no specific action or if --show is specified
    if args.show or not any(vars(args).values()):
        tracker.show_progress()

if __name__ == "__main__":
    main()