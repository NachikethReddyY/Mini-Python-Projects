# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a beginner Python learning project: a command-line to-do list application. The user is learning Python basics including classes, file I/O, and program structure.

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
