def print_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        task = todo_list.pop(task_index - 1)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please try again.")

if __name__ == "__main__":
    todo_list = []

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print_todo_list(todo_list)

        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(todo_list, task)

        elif choice == '3':
            print_todo_list(todo_list)
            task_index = int(input("Enter the task number to remove: "))
            remove_task(todo_list, task_index)

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
