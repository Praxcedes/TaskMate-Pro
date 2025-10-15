from cli.users_menu import users_menu
from cli.projects_menu import projects_menu
from cli.tasks_menu import tasks_menu

def main_menu():
    while True:
        print("\n=== TaskMate Pro Main Menu ===")
        print("1. Manage Users")
        print("2. Manage Projects")
        print("3. Manage Tasks")
        print("0. Exit")

        choice = input("Enter choice: ").strip() 


        if choice == "1":
            users_menu()
        elif choice == "2":
            projects_menu()
        elif choice == "3":
            tasks_menu()
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")