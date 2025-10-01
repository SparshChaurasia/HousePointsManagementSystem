import sys

import admin_interface
import user_interface
from core.login import validate_user
from core.utils import clear_screen


clear_screen()
print("LOGIN")
print("---------------")
username = input("Username: ")
password = input("Password: ")

user = validate_user(username, password)
if user == -1:
    print("Invalid user credentials!")
    sys.exit(0)
clear_screen()

print("================ HOUSE POINTS MANAGEMENT SYSTEM ================")
print(f"USER | {user[0]}")
print("--------------")
print(f"ROLE | {user[1]}\n")

if user[1].lower() == "admin":
    admin_interface.main()

elif user[1].lower() == "user":
    user_interface.main()
