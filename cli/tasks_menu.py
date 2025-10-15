from models.task import Task

def tasks_menu():
    while True:
        print("\n--- Tasks Menu ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Find Task by ID")
        print("4. Mark as Complete")
        print("5. Delete Task")
        print("0. Back")

        choice = input("Enter choice: ").strip()

    if choice == "1":
            title = input("Enter task title: ")
            project_id = int(input("Enter project ID: "))
            Task.create(title, project_id)
            print("✅ Task created!")
            