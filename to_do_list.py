import json
FILE = "tasks.json"
try:
    with open(FILE, "r") as f:
        tasks = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Mark Task Completed")
    print("5. Delete Task")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter a task: ").strip()
        if task:
            tasks.append({"task": task, "completed": False})
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                if tasks[i]["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"
                print(i + 1, ".", tasks[i]["task"], "-", status)
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to edit.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])
            number = int(input("Enter task number to edit: "))
            if 1 <= number <= len(tasks):
                new_task = input("Enter the new task: ").strip()
                if new_task:
                    tasks[number - 1]["task"] = new_task
                    print("Task updated successfully!")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])
            number = int(input("Enter task number to complete: "))
            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as completed!")
            else:4           
            print("Invalid task number.")
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
    elif choice == "6":
        with open(FILE, "w") as f:
            json.dump(tasks, f, indent=4)
        print("Tasks saved. Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)