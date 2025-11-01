# to do list manager where users can add, view, complete, and delete tasks.
def show_menu():
    print("\n---------To-Do List Manager -------------")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

def main():
    tasks = []  # List to store tasks

    while True:
        show_menu()
        choice = int(input("enter your choice (1-5): "))

        if choice == 1:
            print("\n--- Your Tasks ---")
            if not tasks:
                print("No tasks available!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            print("------------------")

        elif choice == 2:
            task = input(" Enter the task to add:").strip()
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == 3:
            task_num = int(input("Enter the task number to complete:"))
            if 1 <= task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)
                print(f"Task '{completed_task}' completed successfully!")
            else:
                print("Invalid task number!")

        elif choice == 4:
            task_num = int(input("Enter the task number to delete:"))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number!")

        elif choice == 5:
            print("Goodbye!")
            break

        else: 
            print("Invalid choice! Please enter a number between 1 and 5.")
        print("-----------------------------------------")

if __name__ == "__main__":
    main()