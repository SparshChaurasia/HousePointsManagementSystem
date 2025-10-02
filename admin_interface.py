from prettytable import PrettyTable, TableStyle

from core.utils import *
from user_interface import *


def add_student(cnx):
    pass


def main():
    table = PrettyTable()
    table.add_rows(
        [
            ["0", "Exit", "6", "Add Event"],
            ["1", "View House Points", "7", "Add Event Participants"],
            ["2", "View Student Points", "8", "Add Event Results"],
            ["3", "View Events", "9", "Activity Report"],
            ["4", "View Event Participants", "10", "Show Menu"],
            ["5", "Add Student", "", ""],
        ]
    )
    table.align = "l"
    table.set_style(TableStyle.SINGLE_BORDER)
    print(table.get_string(header=False))

    cnx = connect_to_database()

    while True:
        print("----------------------------------------------------------------")
        ch = int_input(
            "Enter 10 to show menu",
            (0, 10),
        )

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
            table = PrettyTable()
            table.add_rows(
                [
                    ["0", "Exit", "6", "Add Event"],
                    ["1", "View House Points", "7", "Add Event Participants"],
                    ["2", "View Student Points", "8", "Add Event Results"],
                    ["3", "View Events", "9", "Activity Report"],
                    ["4", "View Event Participants", "10", "Show Menu"],
                    ["5", "Add Student", "", ""],
                ]
            )
            table.align = "l"
            table.set_style(TableStyle.SINGLE_BORDER)
            print(table.get_string(header=False))
        else:
            print("Something went wrong!")
    cnx.close()
    return
