'''
TO-DO LIST
TASK 1
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists

'''

import json
import datetime

def load_tasks(filename='todo.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='todo.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({
        "task": task,
        "completed": False,
        "created_at": datetime.datetime.now().isoformat(),
        "completed_at": None 
    })
    print("Task added successfully!")
    return tasks

def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks):
            prefix = '[x]' if task.get('completed', False) else '[ ]'
            completed_at_str = f" (Completed: {task.get('completed_at', '')})" if task.get('completed_at') else ''
            print(f"{index+1}. {prefix} {task['task']}{completed_at_str}")
    else:
        print("\nYour to-do list is empty.")

def mark_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the number of the task to mark as complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]['completed'] = True
                tasks[index]['completed_at'] = datetime.datetime.now().isoformat() 
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return tasks

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return tasks

def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the number of the task to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter the new task description: ")
                tasks[index]['task'] = new_task
                print("Task updated!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return tasks

def main():
    tasks = load_tasks()

    while True:
        print("Welcome to the To-Do List Application:")
        print("\nChoose an action:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Update task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tasks = add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            tasks = mark_complete(tasks)
        elif choice == '4':
            tasks = delete_task(tasks)
        elif choice == '5':
            tasks = update_task(tasks)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        save_tasks(tasks) 

if __name__ == '__main__':
    main()
