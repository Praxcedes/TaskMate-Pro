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