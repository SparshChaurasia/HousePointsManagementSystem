"""
The main entry point for the House Points Management System application.

This module handles the initial user login process and redirecting control to either the administrator interface or the general user interface based on the user's role.
"""

import sys

import admin_interface
import user_interface
from core.exceptions import InvalidUserCredentials
from core.login import validate_user
from core.utils import clear_screen


def main():
    """
    Executes the main application logic.
    """

    clear_screen()
    print("LOGIN")
    print("----------------------------------------------------------------")

    try:
        username = input("username: ")
        password = input("password: ")
    except KeyboardInterrupt:
        print("\nProgram Exit!")
        sys.exit(0)
    except Exception:
        print("\nAn error occured!")
        sys.exit(0)

    try:
        user = validate_user(username, password)
    except InvalidUserCredentials as e:
        print(e)
        sys.exit(0)

    clear_screen()

    print("---------------- HOUSE POINTS MANAGEMENT SYSTEM ----------------")
    print("USER: ", user[0])
    print("ROLE: ", user[1])

    if user[1].lower() == "admin":
        admin_interface.main()

    elif user[1].lower() == "user":
        user_interface.main()

    print("------------------------- PROGRAM EXIT -------------------------")


if __name__ == "__main__":
    main()
