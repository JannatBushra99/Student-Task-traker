from task_manager import TaskManager

def main():
    manager = TaskManager() 
    manager.load_from_file()  

    while True:
        print("\n====== Student Task Tracker ======")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Task Title: ").strip()
            description = input("Description: ").strip()
            manager.add_task(title=title, description=description)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter Task ID to update: ").strip())
                new_title = input("New Title: ").strip()
                new_description = input("New Description: ").strip()
                manager.update_task(task_id=task_id, new_title=new_title, new_description=new_description)
            except ValueError:
                print("[ERROR] Invalid input! ID must be a number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter Task ID to delete: ").strip())
                manager.delete_task(task_id=task_id)
            except ValueError:
                print("[ERROR] Invalid input! ID must be a number.")

        elif choice == "5":
            print("Saving tasks and exiting...")
            manager.save_to_file()
            break

        else:
            print("[ERROR] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
