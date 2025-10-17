from prettytable import PrettyTable, TableStyle

from core.utils import *
from user_interface import *
from core.exceptions import InputLengthExceeded, InvalidInputLength


def add_student(cnx):
    try:
        stud_id = char_input("Enter student id (length=7) >>> ", length=7).upper()
        adm_no = char_input("Enter admission no. (length=12) >>> ", length=12)
        name = char_input("Enter student name (max_length=50) >>> ", max_length=50)
        house = input_from_choice(
            "Select house —", ["Arun", "Bhaskar", "Ravi", "Martand"]
        )
    except Exception as e:
        print(e)
        return

    points = 0

    cur = create_database_cursor(cnx)
    cur.execute(
        f"INSERT INTO Students VALUES('{stud_id}', '{adm_no}', '{name}', '{house}', {points})"
    )
    cnx.commit()

    print("Record added!")


def add_event(cnx):
    # Automatically generate a new event id
    cur = create_database_cursor(cnx)
    cur.execute("SELECT * FROM Events ORDER BY Id DESC LIMIT 1;")
    prev_id = cur.fetchone()[0]
    if prev_id:
        event_id = prev_id + 1
    else:
        event_id = 1

    cur = create_database_cursor(cnx)
    cur.execute("SELECT Name FROM StudentGroup;")
    options = cur.fetchall()

    try:
        name = char_input("Enter event name (max_length=50) >>> ", max_length=50)
        held_on = date_input("Enter event date (format=YYYY-MM-DD) >>> ")
        event_type = input_from_choice(
            "Select event type —",
            [
                "Interhouse",
                "Interschool",
                "CBSE Cluster",
                "District",
                "State",
                "National",
            ],
        )
        organiser = input_from_choice(
            "Select organiser —", ["School", "CBSE", "Rotary Club"]
        )
        student_group = input_from_choice("Select group —", [i[0] for i in options])
    except Exception as e:
        print(e)
        return

    cur = create_database_cursor(cnx)
    cur.execute(
        f"INSERT INTO Events(Id, Name, HeldOn, StudentGroup, Type, Organiser) VALUES({event_id}, '{name}', '{held_on}', '{student_group}', '{event_type}', '{organiser}');"
    )
    cnx.commit()


def add_event_participants(cnx):
    pass


def add_event_results(cnx):
    pass


def activity_report(cnx):
    pass


def main():
    table = PrettyTable()
    table.add_rows(
        [
            ["0", "Exit", "6", "Add Student"],
            ["1", "Show Menu", "7", "Add Event"],
            ["2", "View House Points", "8", "Add Event Participants"],
            ["3", "View Student Points", "9", "Add Event Results"],
            ["4", "View Event Details", "10", "Activity Report"],
            ["5", "View Event Participants", "", ""],
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
            (0, 10),
        )

        if ch == -1:
            continue

        elif ch == 0:
            break

        elif ch == 1:
            table = PrettyTable()
            table.add_rows(
                [
                    ["0", "Exit", "6", "Add Student"],
                    ["1", "Show Menu", "7", "Add Event"],
                    ["2", "View House Points", "8", "Add Event Participants"],
                    ["3", "View Student Points", "9", "Add Event Results"],
                    ["4", "View Event Details", "10", "Activity Report"],
                    ["5", "View Event Participants", "", ""],
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

        elif ch == 6:
            add_student(cnx)

        elif ch == 7:
            add_event(cnx)

        elif ch == 8:
            add_event_participants(cnx)

        elif ch == 9:
            add_event_results(cnx)

        elif ch == 10:
            activity_report(cnx)

        else:
            print("Something went wrong!")

    cnx.close()
