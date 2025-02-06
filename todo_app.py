
tasks = []  # قائمة لتخزين المهام

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the task number to delete: "))
            if 1 <= task_index <= len(tasks):
                tasks.pop(task_index - 1)
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the app.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
