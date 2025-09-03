# @title 2. To-Do List Application

"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""

import json
import os

# Simple To-Do List Application


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else "✗"
        print(f"{index}. [{status}] {task['name']}")


def add_task(tasks, task_name):
    tasks.append({"name": task_name, "completed": False})
    print(f"Task added: {task_name}")


def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Task removed: {removed['name']}")
    else:
        print("Invalid task index.")


def mark_task_complete(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Task marked as complete: {tasks[task_index]['name']}")
    else:
        print("Invalid task index.")


def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []


def save_tasks(filename, tasks):
    with open(filename, 'w') as f:
        json.dump(tasks, f)


def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)
    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task Complete")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
            save_tasks(filename, tasks)
        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, task_index)
            save_tasks(filename, tasks)
        elif choice == "3":
            task_index = int(input("Enter task index to mark complete: ")) - 1
            mark_task_complete(tasks, task_index)
            save_tasks(filename, tasks)
        elif choice == "4":
            save_tasks(filename, tasks)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
