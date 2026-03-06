import os
import json
import datetime

# A program to add, view, remove, and complete tasks, storing them in a JSON file.

# Initialisation
# Tasks = json.array[]
# Inside python projects, JSON is just writen as an array.
tasks = []


# Add
# def add(New_task):
#     tasks.append(New_task)

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
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            task.display()

    def complete_task(self, index):
        task = self.tasks[index]
        task.mark_complete()

    def remove_task(self, index):
        self.tasks.pop(index)

    def save_to_file(self):
        data = []
        for task in self.tasks:
            task.dict = {
                "description": task.description,
                "completed": task.completed,
                "created_at": task.created_at.isoformat()
            }
            data.append(task.dict)
        with open("tasks.json", "w") as file:
            json.dump(data, file)

    def load_from_file(self):
        if not os.path.exists("tasks.json"):  # Check file exists first
            return  # Nothing to load yet

        with open("tasks.json", "r") as file:
            data = json.load(file)
        self.tasks = []
        for item in data:                    # Use 'item' consistently
            task = Task(item["description"]) # Now 'item' exists
            task.completed = item["completed"]
            task.created_at = datetime.datetime.fromisoformat(item["created_at"])
            self.tasks.append(task)


# Menu
def main():
    """
    Main program loop. This function:
    1. Creates a TaskManager instance
    2. Loads any existing tasks from file
    3. Shows the menu in a loop until user chooses to exit
    4. Routes user input to the appropriate TaskManager methods
    5. Saves tasks to file before exiting
    """
    # Create a TaskManager instance to manage all tasks
    manager = TaskManager()

    # Load any previously saved tasks from tasks.json
    # If the file doesn't exist, load_from_file() returns silently
    manager.load_from_file()

    # Show the welcome banner once at startup
    print(f"""Hello!
Welcome to task manager with python!

These are your tasks today!

You have {len(manager.tasks)} tasks!""")

    # Main program loop - keeps showing menu until user exits
    # while True creates an infinite loop that we break out of with 'break'
    while True:
        # Display the compact menu (without the welcome banner)
        print("""
What would you like to do?
1. Add New Task
2. Complete a Task
3. View all the tasks.
4. Remove a task
5. Save and Exit""")

        # Get user input as a string
        user_input = input("\nEnter a Number Here: ")

        # Route the user's choice to the appropriate action
        # Each if/elif checks which option was selected

        if user_input == "1":
            # Option 1: Add a new task
            description = input("Enter task description: ")
            manager.add_task(description)
            print(f"Task added: {description}")
            input("\nPress Enter to continue...")

        elif user_input == "2":
            # Option 2: Complete a task
            # First show all tasks so user can see the numbers
            manager.view_tasks()
            # Get the task number and convert to 0-based index
            # We subtract 1 because users see 1, 2, 3 but Python uses 0, 1, 2
            index = int(input("Enter task number to complete: ")) - 1
            manager.complete_task(index)
            print("Task marked as complete!")
            input("\nPress Enter to continue...")

        elif user_input == "3":
            # Option 3: View all tasks
            manager.view_tasks()
            input("\nPress Enter to continue...")

        elif user_input == "4":
            # Option 4: Remove a task
            # Show tasks first so user knows which number to enter
            manager.view_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            manager.remove_task(index)
            print("Task removed!")
            input("\nPress Enter to continue...")

        elif user_input == "5":
            # Option 5: Save and exit
            # Save all tasks to tasks.json file
            manager.save_to_file()
            print("Tasks saved. Goodbye!")
            # break exits the while True loop, ending the program
            break

        else:
            # Handle invalid input (anything other than 1-5)
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")


# This is a standard Python pattern that checks if this file is being run directly
# __name__ is a special variable that Python sets automatically:
#   - When you run: python main.py → __name__ == "__main__" → main() is called
#   - When you import: import main → __name__ == "main" → main() is NOT called
# This allows other programs to import your Task/TaskManager classes without
# running the menu automatically
if __name__ == "__main__":
    main()
