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

        