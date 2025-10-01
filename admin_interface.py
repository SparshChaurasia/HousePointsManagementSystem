from core.utils import *
from user_interface import *


def add_student(cnx):
    pass


def main():
    print(
        "0. Exit\n1. View House Points\n2. View Student Points\n3. View Events\n4. View Event Participants"
        "5. Add Student\n6. Add Event\n7. Add Event Participants\n8. Add Event Results\n9. Activity Report\n10. Show Menu\n"
    )
    cnx = connect_to_database()

    while True:
        ch = int_input("Enter 10 to show menu", (0, 10))
        print("ch value is: ", ch)
        if ch == -1:
            continue
        elif ch == 0:
            break
        elif ch == 1:
            view_house_points(cnx)
        elif ch == 2:
            view_student_points(cnx)
        elif ch == 3:
            view_events(cnx)
        elif ch == 4:
            view_event_participants(cnx)
        elif ch == 10:
            print(
                "0. Exit\n1. View House Points\n2. View Student Points\n3. View Events\n4. View Event Participants"
                "5. Add Student\n6. Add Event\n7. Add Event Participants\n8. Add Event Results\n9. Activity Report\n10. Show Menu\n"
            )
        else:
            print("Something went wrong!")
    cnx.close()
    return
