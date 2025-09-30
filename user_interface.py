from core.utils import *


def view_house_points(cnx):
    cur = create_database_cursor(cnx)
    cur.execute("SELECT Name, Points FROM Houses;")
    print_queryset(cur)


def view_student_points(cnx):
    ch = input_choice("\n0. Exit\n1. Search by ID\n2. Show all")

    if ch == -1:
        print("Error")
    elif ch == 0:
        print("Error")
    elif ch == 1:
        stud_id = int(input("Enter Student ID >> "))
        cur = create_database_cursor(cnx)
        cur.execute(f"SELECT Name, Points FROM Students WHERE Id={stud_id};")
        print_queryset(cur)
    elif ch == 2:
        cur = create_database_cursor(cnx)
        cur.execute(f"SELECT Id, Name, House, Points FROM Students;")
        print_queryset(cur)


def view_events(cnx):
    cur = create_database_cursor(cnx)
    cur.execute("SELECT * FROM Events;")
    print_queryset(cur)


def view_event_participants(cnx):
    ch = input_choice("\n0. Exit\n1. Search by Event\n2. Show all")

    if ch == -1:
        print("Error")
    elif ch == 0:
        print("Error")
    elif ch == 1:
        event_id = int(input("Enter Event ID >> "))
        cur = create_database_cursor(cnx)
        cur.execute(f"SELECT * FROM Participations WHERE EventId={event_id};")
        print_queryset(cur)
    elif ch == 2:
        cur = create_database_cursor(cnx)
        cur.execute(f"SELECT * FROM Participations;")
        print_queryset(cur)


def main():
    print(
        "0. Exit\n1. View House Points\n2. View Student Points\n3. View Events\n4. View Event Participants"
    )

    cnx = connect_to_database()

    while True:
        ch = input_choice("Enter 8 to show menu")

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
        elif ch == 8:
            print(
                "0. Exit\n1. View House Points\n2. View Student Points\n3. View Events\n4. View Event Participants"
            )

    cnx.close()
