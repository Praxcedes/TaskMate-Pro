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
            