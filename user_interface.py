"""
Provides a command-line interface for viewing database records for user related tasks such as viewing house points, student points, and event details etc.
"""

from prettytable import PrettyTable, TableStyle

from core.utils import *


def view_house_points(cnx):
    """
    Retrieves and prints the name and total points for all houses.

    Args:
        cnx: The active database connection object.
                
    Returns:
        None
    """
    try:
        cur = create_database_cursor(cnx)
        cur.execute("SELECT Name, Points FROM Houses ORDER BY Points DESC")
        print_queryset(cur)
    except Exception as e:
        print(e)
        return


def view_student_points(cnx):
    """
    Displays a menu to view student points, allowing the user to search by student ID or view all students.

    Args:
        cnx: The active database connection object.
            
    Returns:
        None
    """

    try:
        ch = int_input("\n0. Exit\n1. Search by ID\n2. Show all\n>>> ")

        if ch == 0:
            return
        elif ch == 1:
            stud_id = char_input("Enter Student ID >>> ").upper()
            cur = create_database_cursor(cnx)
            cur.execute(f"SELECT Id, Name, House, Points FROM Students WHERE Id='{stud_id}'")
            print_queryset(cur)
        elif ch == 2:
            cur = create_database_cursor(cnx)
            cur.execute(f"SELECT Id, Name, House, Points FROM Students")
            print_queryset(cur)

    except Exception as e:
        print(e)
        return


def view_events(cnx):
    """
    Retrieves and prints all records from the Events table.

    Args:
        cnx: The active database connection object.
            
    Returns:
        None
    """
    try:
        cur = create_database_cursor(cnx)
        cur.execute("SELECT * FROM Events")
        print_queryset(cur)

    except Exception as e:
        print(e)
        return


def view_event_participants(cnx):
    """
    Displays a menu to view event participants, allowing the user to search by event ID or view all participations.

    Args:
        cnx: The active database connection object.
            
    Returns:
        None
    """

    try:
        ch = int_input("\n0. Exit\n1. Search by Event\n2. Show all\n>>> ")  

        if ch == 0:
            return
        elif ch == 1:
            event_id = int_input("Enter Event ID >>> ")
            cur = create_database_cursor(cnx)
            cur.execute(
                f"SELECT (SELECT Name FROM Events WHERE Id=Participations.EventId) AS EventName, (SELECT Name FROM Students WHERE Id=Participations.StudentId) AS StudentName, PointsAwarded FROM Participations WHERE Participations.EventId={event_id}"
            )
            print_queryset(cur)
        elif ch == 2:
            cur = create_database_cursor(cnx)
            cur.execute(
                f"SELECT (SELECT Name FROM Events WHERE Id=Participations.EventId) AS EventName, (SELECT Name FROM Students WHERE Id=Participations.StudentId) AS StudentName, PointsAwarded FROM Participations"
            )
            print_queryset(cur)

    except Exception as e:
        print(e)
        return


def main():
    """
    The main execution function for the user interface.
    """

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
        try:
            ch = int_input(
                message="Enter 1 to show menu\n>>> ",
                rng=(0, 5),
            )
        except Exception as e:
            print(e)
            continue

        if ch == 0:
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
