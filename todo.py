import os

# Function to display the tasks
def display_tasks(tasks):
    if len(tasks) == 0:
        print("Your To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the task number you want to delete: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' has been deleted.")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the task number you want to mark as complete: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] += " (Completed)"
        print(f"Task '{tasks[task_number - 1]}' has been marked as completed.")
    else:
        print("Invalid task number.")

# Main function to control the flow of the program
def main():
    tasks = []  # List to store the tasks
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
