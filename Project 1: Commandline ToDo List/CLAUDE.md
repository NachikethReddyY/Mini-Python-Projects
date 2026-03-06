# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a beginner Python learning project: a command-line to-do list application. The user is learning Python basics
including classes, file I/O, and program structure.

**Important Context:**

- This is an educational project - the user is learning Python fundamentals
- Always use "Learning" output style with "Learn by Doing" sections
- The user writes the code; you provide guidance and review
- Use TODO(human) comments to mark sections for the user to implement

## Architecture

The application follows a two-class design:

### Task Class

Represents a single task with its data and behaviors.

- `description`: The task text
- `created_at`: Timestamp when task was created (datetime)
- `completed`: Boolean status
- Methods: `mark_complete()`, `display()`

### TaskManager Class

Manages the collection of tasks and handles persistence.

- `tasks`: List of Task objects
- Methods: `add_task()`, `view_tasks()`, `complete_task()`, `remove_task()`, `save_to_file()`, `load_from_file()`

### Menu System

Simple console-based menu that:

1. Displays welcome message and task count
2. Shows options (Add, Complete, View, Remove)
3. Accepts user input and routes to appropriate TaskManager method

## Running the Application

```bash
# Run the main application
python main.py

# No build step required - this is a simple Python script
# No test suite set up yet
```

## File Structure

```
main.py              # Main application file (contains Task, TaskManager, menu)
tasks.json           # Data file (created at runtime)
```

## Dependencies

Standard library only:

- `json` - For file persistence
- `os` - For file operations
- `datetime` - For task timestamps

## Development Mode

When working with this user:

1. Use TODO(human) comments to mark implementation sections
2. Ask the user to write code before reviewing
3. Explain errors conceptually before offering fixes
4. Frame contributions as design decisions in "Learn by Doing" sections
5. Wait for user implementation before proceeding to next feature

## Current Implementation Context (2026-03-06)

### User's Understanding Level

- ✅ **Classes and `self`**: Understood well - Task class is correct
- ⚠️ **Instance attributes**: Partially understood - missed `self.tasks` in TaskManager.__init__
- ⚠️ **List operations on objects**: Needs clarification - confused about which object has methods
- 🆕 **File I/O and JSON**: New concept - needs explanation of serialization/deserialization

### Common Mistakes to Watch For

- `self` is not a list - can't call `self.append()` or `self.pop()`
- Must access the actual list attribute: `self.tasks.append()`, `self.tasks.pop(index)`
- Must access task via index before calling methods: `self.tasks[index].mark_complete()`

### JSON Persistence Requirements

- Task objects must be converted to dictionaries before saving
- datetime objects need `.isoformat()` / `fromisoformat()` conversion
- File operations need `with open(...)` context manager
- Check file existence with `os.path.exists()` before loading

---

## Project Completion Summary

### What I Learned

Through building this project, I learned:

1. **Python Classes and Objects**
    - How to define classes with `class` keyword
    - The `__init__` constructor method for initialization
    - Using `self` to access instance attributes and methods
    - Creating methods that operate on object data

2. **Object-Oriented Design**
    - Separation of concerns: `Task` for data, `TaskManager` for operations
    - How classes can work together (TaskManager uses Task objects)
    - Why storing data on `self` matters for persistence across method calls

3. **File I/O and JSON Persistence**
    - The `with open(...)` context manager pattern for safe file handling
    - Converting objects to dictionaries for JSON serialization
    - Handling datetime objects with `.isoformat()` and `.fromisoformat()`
    - Checking file existence before reading

4. **Python Control Flow**
    - `while True` loops with `break` for menu systems
    - `if/elif/else` for routing user input
    - Converting between 1-based user input and 0-based list indices

5. **The `__name__ == "__main__"` Pattern**
    - Why we use this guard to control program execution
    - How it enables code reuse through importing without auto-running
    - The difference between running a file directly vs importing it

### What I Wrote

I implemented all the core functionality:

- **Task class**: Complete with `__init__`, `mark_complete()`, and `display()` methods
- **TaskManager class**: All seven methods implemented:
    - `__init__()` - Initialize task list
    - `add_task()` - Create and add Task objects
    - `view_tasks()` - Display all tasks
    - `complete_task()` - Mark tasks as complete by index
    - `remove_task()` - Remove tasks by index
    - `save_to_file()` - Convert tasks to JSON and save
    - `load_from_file()` - Load JSON and recreate Task objects

### How Claude Code Helped Me

Claude Code helped me through this learning journey by:

1. **Providing conceptual explanations** before showing code, ensuring I understood the "why" before the "how"

2. **Reviewing my code iteratively** - I would write code, Claude would identify specific issues and explain what was
   wrong conceptually, then I would fix it

3. **Explaining common mistakes** like confusing `self` with the list attribute, mixing up `json.dump` vs `json.load`,
   and variable scope issues

4. **Teaching new concepts** like the `with open()` context manager, JSON serialization/deserialization, and the
   `__name__ == "__main__"` pattern with clear examples

5. **Adding the menu system** after I completed all the class implementations, showing how the pieces fit together

6. **Adding comprehensive comments** to explain the code flow and serve as a reference for future learning

Claude Code acted as a patient tutor, never writing the code for me until I had attempted it myself, which helped
reinforce my learning through practice and mistakes.

---
