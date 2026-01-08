tasks = []

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1: Add task")
    print("2: View tasks")
    print("3: Delete task")
    print("4: Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        # Add new task
        new_task = input("Enter your task: ")
        tasks.append(new_task)
        print("Task added successfully.")

    elif choice == "2":
        # View tasks
        if not tasks:
            print("Your task list is empty.")
        else:
            print("\nYour current tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")

    elif choice == "3":
        # Delete a task
        if not tasks:
            print("Nothing to delete.")
        else:
            print("\nChoose the number of the task to delete:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
            try:
                task_num = int(input("Task number: "))
                removed = tasks.pop(task_num - 1)
                print(f"Deleted: '{removed}'")
            except (ValueError, IndexError):
                print("Invalid number.")

    elif choice == "4":
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
