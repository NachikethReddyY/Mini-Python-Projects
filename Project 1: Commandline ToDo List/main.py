# import os
# import json
import datetime

# A program to add, view, remove, and complete tasks, storing them in a JSON file.

# Initialisation
# Tasks_json = json.array[]
# Inside python projects, json is just writen as an array.
tasks = []

# Add
# def add(Newtask):
#     tasks.append(Newtask)

# View
# def View(tasks):
#     print (tasks)

# Remove

# Complete


# TODO(human): Implement the Task class here
# The Task class should have:
#   - __init__(self, description): stores description, created_at, completed
#   - mark_complete(self): sets completed to True
#   - display(self): returns formatted string with [✓] or [ ] + description
class Task:
    def __init__(self, description):
        self.description = description
        self.created_at = datetime.datetime.now()
        self.completed = False
    def mark_complete(self):
        self.completed = True
    def display(self):
        status = "[✓]" if self.completed else "[ ]"
        print(f"{status} {self.description}")


# TODO(human): Implement the TaskManager class here
# The TaskManager class should manage a collection of Task objects:
#   - __init__(self): Initialize with an empty list for tasks
#   - add_task(self, description): Create a new Task and add to the list
#   - view_tasks(self): Loop through tasks and call display() on each
#   - complete_task(self, index): Mark a task at given index as complete
#   - remove_task(self, index): Remove task at given index
#   - save_to_file(self): Save tasks to JSON file
#   - load_from_file(self): Load tasks from JSON file


# Menu
print(f"""Hello!
Welcome to task manager with python!

These are your tasks today!

You have {len(tasks)} tasks!


What would you like to do?
1. Add New Task
2. Complete a Task
3. View all the tasks.
4. Remove a task

Enter a Number.
""")

user_input = input("Enter a Number Here: ")


print(f"You have entered {user_input}")

