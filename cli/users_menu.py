from models.user import User

def users_menu():
    while True:
        print("\n--- Users Menu ---")
        print("1. Add User")
        print("2. View All Users")
        print("3. Find User by ID")
        print("4. Delete User")
        print("0. Back")

        choice = input("Enter choice: ").strip()


        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            User.create(name, email)
            print("✅ User created successfully!")
            