import sys
from core.login import validate_user
from core.utils import clear_screen

print("LOGIN")
print("-----")
username = input("Username: ")
password = input("Password: ")

user = validate_user(username, password)
if user == -1:
    print("Invalid user credentials")
    sys.exit(0)
clear_screen()

print("================ HOUSE POINTS MANAGEMENT SYSTEM ================")
print(f"USER | {user[0]}")
print("--------------")
print(f"ROLE | {user[1]}\n")

print(
    "0. Exit\n1. View House Points\n2. View Student Points\n3. View Events\n4. View Event Participants"
)
print(
    "5. Add Student\n6. Add Event\n7. Add Event Participants\n8. Add Event Results\n9. Activity Report\n10. Show Menu\n"
)

cnx = connect_to_database()

while True:
    ch = input_choice("Enter 8 to show menu")

    if ch == -1:
        continue

    elif ch == 0:
        break

    elif ch == 1:
        cur = create_database_cursor(cnx)
        cur.execute("SELECT Name, Points FROM Houses;")
        print_queryset(cur)

    elif ch == 2:
        ch = input_choice("\n0. Exit\n1. Search by ID\n2. Show all")

        if ch == -1:
            continue
        elif ch == 0:
            break
        elif ch == 1:
            stud_id = int(input("Enter Student ID >> "))
            cur = create_database_cursor(cnx)
            cur.execute(f"SELECT Name, Points FROM Students WHERE Id={stud_id};")
            print_queryset(cur)
        elif ch == 2:
            cur = create_database_cursor(cnx)
            cur.execute(f"SELECT Id, Name, House, Points FROM Students;")
            print_queryset(cur)

    elif ch == 3:
        cur = create_database_cursor(cnx)
        cur.execute("SELECT * FROM Events;")
        print_queryset(cur)

    elif ch == 4:
        ch = input_choice("\n0. Exit\n1. Search by Event\n2. Show all")

        if ch == -1:
            continue
        elif ch == 0:
            break
        elif ch == 1:
            event_id = int(input("Enter Event ID >> "))
            cur = create_database_cursor(cnx)
            cur.execute(f"SELECT * FROM Participations WHERE EventId={event_id};")
            print_queryset(cur)
        elif ch == 2:
            cur = create_database_cursor(cnx)
            cur.execute(f"SELECT * FROM Participations;")
            print_queryset(cur)

    elif ch == 8:
        print(
            "0. Exit\n1. View House Points\n2. View Student Points\n3. View Events\n4. View Event Participants"
        )
        print("5. Add Student\n6. Add Event\n7. Add Event Participants\n8. Show Menu\n")

cnx.close()
