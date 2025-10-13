tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"'{task}' has been added!\n")

def view_tasks():
    if not tasks:
        print("No tasks added yet!\n")
        return
    print("\nYour To-Do List:")
    for index, item in enumerate(tasks, start=1):
        status = "Done" if item["completed"] else "Not Done"
        print(f"{index}. {item['task']} - {status}")
    print()

def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        deleted = tasks.pop(task_number - 1)
        print(f"'{deleted['task']}' has been deleted!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

while True:
    print("====== TO-DO LIST APP ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
