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

    elif choice == "2":
            for t in Task.get_all():
                print(f"{t.id}. {t.title} - {t.status} (Project ID: {t.project_id})")
    elif choice == "3":
            id = int(input("Enter task ID: "))
            t = Task.find_by_id(id)
            print(t.__dict__ if t else "❌ Task not found.")
    elif choice == "4":
            id = int(input("Enter task ID to mark complete: "))
            t = Task.find_by_id(id)
            if t:
                t.mark_complete()
                print("✅ Task marked complete!")
            else:
                print("❌ Task not found.")
    elif choice == "5":
            id = int(input("Enter task ID to delete: "))
            t = Task.find_by_id(id)
            if t:
                t.delete()
                print("🗑️ Task deleted.")
            else:
                print("❌ Task not found.")
    elif choice == "0":
       break
         else:
            print("Invalid choice.")