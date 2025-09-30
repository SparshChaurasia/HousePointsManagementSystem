import sys

import admin_interface
import user_interface
from core.login import validate_user
from core.utils import clear_screen
from core.exceptions import InterfaceExit

while True:
    print("LOGIN")
    print("-----")
    username = input("Username: ")
    password = input("Password: ")

    user = validate_user(username, password)
    if user == -1:
        print("Invalid user credentials")
        sys.exit(0)
    # clear_screen()

    print("================ HOUSE POINTS MANAGEMENT SYSTEM ================")
    print(f"USER | {user[0]}")
    print("--------------")
    print(f"ROLE | {user[1]}\n")

    if user[1].lower() == "admin":
        try:
            admin_interface.main()
        except InterfaceExit:
            print("exception raised")
            pass
    elif user[1].lower() == "user":
        user_interface.main()
