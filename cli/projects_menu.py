from models.project import Project

def projects_menu():
    while True:
        print("\n--- Projects Menu ---")
        print("1. Add Project")
        print("2. View All Projects")
        print("3. Find Project by ID")
        print("4. Delete Project")
        print("0. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter project name: ")
            user_id = int(input("Enter user ID: "))
            Project.create(name, user_id)
            print("✅ Project created successfully!")
        elif choice == "2":
            for p in Project.get_all():
                print(f"{p.id}. {p.name} (User ID: {p.user_id})")
        elif choice == "3":
            id = int(input("Enter project ID: "))
            project = Project.find_by_id(id)
            print(project.__dict__ if project else "❌ Project not found.")
        elif choice == "4":
            id = int(input("Enter project ID to delete: "))
            project = Project.find_by_id(id)
            if project:
                project.delete()
                print("🗑️ Project deleted.")
            else:
                print("❌ Project not found.")