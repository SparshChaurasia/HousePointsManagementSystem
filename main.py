import mysql.connector
from mysql.connector import errorcode
from prettytable import from_db_cursor


def connect_to_database():
    try:
        cnx = mysql.connector.connect(
            user="root",
            password="tiger",
            host="127.0.0.1",
            database="HousePointsManagementSystem",
        )

        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def create_database_cursor(cnx):
    try:
        cur = cnx.cursor()

        return cur
    except mysql.connector.Error as err:
        print("Error in creating cursor")
        print(err)


def print_queryset(cur):
    table = from_db_cursor(cur)
    print(table)


def input_choice(msg):
    try:
        print(msg)
        ch = int(input(">>> "))
        return ch
    except:
        print("Please enter a valid choice / number")
        return -1


if __name__ == "__main__":
    print("-------------- HOUSE POINTS MANAGEMENT SYSTEM --------------")
    print(
        "0. Exit\n1. View House Points\n2. View Student Points\n3. View Events\n4. View Event Participants"
    )
    print("5. Add Student\n6. Add Event\n7. Add Event Participants\n8. Show Menu\n")

    cnx = connect_to_database()

    while True:
        ch = input_choice("Enter 8 to show menu")

        if ch == -1:
            continue

        elif ch == 0:
            break

        elif ch == 1:
            cur = create_database_cursor(cnx)
            cur.execute("SELECT * FROM Houses;")
            print_queryset(cur)

        elif ch == 2:
            stud_id = int(input("Enter Student ID >> "))
            cur = create_database_cursor(cnx)
            cur.execute(f"SELECT * FROM Students WHERE Id={stud_id};")
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
            print(
                "5. Add Student\n6. Add Event\n7. Add Event Participants\n8. Show Menu\n"
            )

    cnx.close()
