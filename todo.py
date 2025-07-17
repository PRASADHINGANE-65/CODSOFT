tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i+1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks.pop(task_no)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")