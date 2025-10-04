from core.utils import *
from prettytable import PrettyTable, TableStyle


def view_house_points(cnx):
    cur = create_database_cursor(cnx)
    cur.execute("SELECT Name, Points FROM Houses;")
    print_queryset(cur)


def view_student_points(cnx):
    ch = int_input("\n0. Exit\n1. Search by ID\n2. Show all")

    if ch == -1:
        return

    elif ch == 0:
        return

    elif ch == 1:
        stud_id = int(input("Enter Student ID >> "))
        cur = create_database_cursor(cnx)
        cur.execute(f"SELECT Id, Name, House, Points FROM Students WHERE Id={stud_id};")
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
    ch = int_input("\n0. Exit\n1. Search by Event\n2. Show all")

    if ch == -1:
        return

    elif ch == 0:
        return

    elif ch == 1:
        event_id = int(input("Enter Event ID >> "))
        cur = create_database_cursor(cnx)
        cur.execute(
            f"SELECT (SELECT Name FROM Events WHERE Id=Participations.EventId) AS EventName, (SELECT Name FROM Students WHERE Id=Participations.StudentId) AS StudentName, PointsAwarded FROM Participations WHERE Participations.EventId={event_id};"
        )
        print_queryset(cur)

    elif ch == 2:
        cur = create_database_cursor(cnx)
        cur.execute(
            f"SELECT (SELECT Name FROM Events WHERE Id=Participations.EventId) AS EventName, (SELECT Name FROM Students WHERE Id=Participations.StudentId) AS StudentName, PointsAwarded FROM Participations;"
        )
        print_queryset(cur)


def main():
    table = PrettyTable()
    table.add_rows(
        [
            ["0", "Exit"],
            ["1", "Show Menu"],
            ["2", "View House Points"],
            ["3", "View Student Points"],
            ["4", "View Event Details"],
            ["5", "View Event Participants"],
        ]
    )
    table.align = "l"
    table.set_style(TableStyle.SINGLE_BORDER)
    print(table.get_string(header=False))

    cnx = connect_to_database()

    while True:
        print("----------------------------------------------------------------")
        ch = int_input(
            "Enter 1 to show menu",
            (0, 5),
        )

        if ch == -1:
            continue

        elif ch == 0:
            break

        elif ch == 1:
            table = PrettyTable()
            table.add_rows(
                [
                    ["0", "Exit"],
                    ["1", "Show Menu"],
                    ["2", "View House Points"],
                    ["3", "View Student Points"],
                    ["4", "View Event Details"],
                    ["5", "View Event Participants"],
                ]
            )
            table.align = "l"
            table.set_style(TableStyle.SINGLE_BORDER)
            print(table.get_string(header=False))

        elif ch == 2:
            view_house_points(cnx)

        elif ch == 3:
            view_student_points(cnx)

        elif ch == 4:
            view_events(cnx)

        elif ch == 5:
            view_event_participants(cnx)

        else:
            print("Something went wrong!")

    cnx.close()
