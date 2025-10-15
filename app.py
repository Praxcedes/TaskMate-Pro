from db.connection import initialize_db
from cli.main_menu import main_menu

if __name__ == "__main__":
    initialize_db()
    main_menu()
