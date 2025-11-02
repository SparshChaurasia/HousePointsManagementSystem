from prettytable import PrettyTable, TableStyle

from core.utils import *
from user_interface import *
from core.exceptions import InputLengthExceeded, InvalidInputLength


def add_student(cnx):
    """
    Adds a new student to the database.
    
    Args:
        cnx: The database connection object.
        
    Returns:
        None
    """
    try:
        stud_id = char_input("Enter student id (length=7) >>> ", length=7)
        if stud_id == -1 or stud_id is None:
            return
        stud_id = stud_id.upper()
        
        adm_no = char_input("Enter admission no. (length=12) >>> ", length=12)
        if adm_no == -1 or adm_no is None:
            return
            
        name = char_input("Enter student name (max_length=50) >>> ", max_length=50)
        if name == -1 or name is None:
            return
            
        house = input_from_choice(
            "Select house —", ["Arun", "Bhaskar", "Ravi", "Martand"]
        )
        if house is None:
            return
    except Exception as e:
        print(e)
        return

    points = 0

    cur = create_database_cursor(cnx)
    if cur is None:
        print("Failed to create database cursor!")
        return
    cur.execute(
        f"INSERT INTO Students VALUES('{stud_id}', '{adm_no}', '{name}', '{house}', {points})"
    )
    cnx.commit()

    print("Record added!")


def add_event(cnx):
    """
    Adds a new event to the database.
    
    Args:
        cnx: The database connection object.
        
    Returns:
        None
    """
    # Automatically generate a new event id
    cur = create_database_cursor(cnx)
    if cur is None:
        print("Failed to create database cursor!")
        return
    cur.execute("SELECT * FROM Events ORDER BY Id DESC LIMIT 1;")
    result = cur.fetchone()
    if result:
        prev_id = result[0]
        event_id = prev_id + 1
    else:
        event_id = 1

    cur = create_database_cursor(cnx)
    if cur is None:
        print("Failed to create database cursor!")
        return
    cur.execute("SELECT Name FROM StudentGroup;")
    options_result = cur.fetchall()
    if options_result is None:
        print("Failed to fetch student groups!")
        return
    options = options_result

    try:
        name = char_input("Enter event name (max_length=50) >>> ", max_length=50)
        if name == -1 or name is None:
            return
            
        held_on = date_input("Enter event date (format=YYYY-MM-DD) >>> ")
        if held_on is None:
            return
            
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
        if event_type is None:
            return
            
        organiser = input_from_choice(
            "Select organiser —", ["School", "CBSE", "Rotary Club"]
        )
        if organiser is None:
            return
            
        student_group = input_from_choice("Select group —", [i[0] for i in options])
        if student_group is None:
            return
    except Exception as e:
        print(e)
        return

    cur = create_database_cursor(cnx)
    if cur is None:
        print("Failed to create database cursor!")
        return
    cur.execute(
        f"INSERT INTO Events(Id, Name, HeldOn, StudentGroup, Type, Organiser) VALUES({event_id}, '{name}', '{held_on}', '{student_group}', '{event_type}', '{organiser}');"
    )
    cnx.commit()


def add_event_participants(cnx):
    """
    Adds a student as a participant to an event with points awarded.
    
    Args:
        cnx: The database connection object.
        
    Returns:
        None
    """
    try:
        # Get event ID
        event_id = int_input("Enter event ID")
        if event_id == -1:
            return
        
        # Check if event exists
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute(f"SELECT Id FROM Events WHERE Id = {event_id}")
        result = cur.fetchone()
        if not result:
            print("Event not found!")
            return
            
        # Get student ID
        stud_id = char_input("Enter student ID (length=7) >>> ", length=7)
        if stud_id == -1 or stud_id is None:
            return
        stud_id = stud_id.upper()
        
        # Check if student exists
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute(f"SELECT Id FROM Students WHERE Id = '{stud_id}'")
        result = cur.fetchone()
        if not result:
            print("Student not found!")
            return
            
        # Get points awarded
        points = int_input("Enter points awarded")
        if points == -1:
            return
            
        # Check if participation already exists
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute(f"SELECT Id FROM Participations WHERE EventId = {event_id} AND StudentId = '{stud_id}'")
        if cur.fetchone():
            print("Participation record already exists!")
            return
        
        cur = create_database_cursor(cnx)
        cur.execute("SELECT Id FROM Participations")
        total_records = len(cur.fetchall())

        # Insert participation record
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute(
            f"INSERT INTO Participations(Id, EventId, StudentId, PointsAwarded) VALUES({total_records + 1}, {event_id}, '{stud_id}', {points})"
        )
        cnx.commit()
        
        print("Participant added successfully!")
        
    except Exception as e:
        print(f"Error adding participant: {e}")


def add_event_results(cnx):
    """
    Records the results of an event by house positions and distributes points accordingly.
    
    Args:
        cnx: The database connection object.
        
    Returns:
        None
    """
    try:
        # Get event ID
        event_id = int_input("Enter event ID")
        if event_id == -1:
            return
            
        # Check if event exists
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute(f"SELECT Id FROM Events WHERE Id = {event_id}")
        result = cur.fetchone()
        if not result:
            print("Event not found!")
            return
            
        # Get position results
        print("Enter house positions:")
        first_position = input_from_choice(
            "Select 1st position house —", 
            ["Arun", "Bhaskar", "Ravi", "Martand"]
        )
        if first_position is None:
            return
        
        second_position = input_from_choice(
            "Select 2nd position house —", 
            ["Arun", "Bhaskar", "Ravi", "Martand"]
        )
        if second_position is None:
            return
        
        # Ensure different houses for positions
        if second_position == first_position:
            print("Same house cannot have multiple positions!")
            return
            
        third_position = input_from_choice(
            "Select 3rd position house —", 
            ["Arun", "Bhaskar", "Ravi", "Martand"]
        )
        if third_position is None:
            return
        
        # Ensure different houses for positions
        if third_position == first_position or third_position == second_position:
            print("Same house cannot have multiple positions!")
            return
            
        fourth_position = input_from_choice(
            "Select 4th position house —", 
            ["Arun", "Bhaskar", "Ravi", "Martand"]
        )
        if fourth_position is None:
            return
        
        # Ensure different houses for positions
        if (fourth_position == first_position or 
            fourth_position == second_position or 
            fourth_position == third_position):
            print("Same house cannot have multiple positions!")
            return
            
        # Update event with results
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute(
            f"UPDATE Events SET FirstPositionHouse='{first_position}', "
            f"SecondPositionHouse='{second_position}', "
            f"ThirdPositionHouse='{third_position}', "
            f"FourthPositionHouse='{fourth_position}' "
            f"WHERE Id={event_id}"
        )
        cnx.commit()
        
        # Award points to houses based on positions
        # 1st place = 10 points, 2nd = 8, 3rd = 6, 4th = 4
        points_map = {
            first_position: 10,
            second_position: 8,
            third_position: 6,
            fourth_position: 4
        }
        
        for house, points in points_map.items():
            cur = create_database_cursor(cnx)
            if cur is None:
                print("Failed to create database cursor!")
                continue
            cur.execute(
                f"UPDATE Houses SET Points = Points + {points} WHERE Name = '{house}'"
            )
            
            # Also update individual student points who participated in this event
            cur = create_database_cursor(cnx)
            if cur is None:
                print("Failed to create database cursor!")
                continue
            cur.execute(
                f"UPDATE Students s JOIN Participations p ON s.Id = p.StudentId "
                f"SET s.Points = s.Points + {points} "
                f"WHERE s.House = '{house}' AND p.EventId = {event_id}"
            )
            
        cnx.commit()
        
        print("Event results added successfully!")
        
    except Exception as e:
        print(f"Error adding event results: {e}")


def activity_report(cnx):
    """
    Generates a comprehensive activity report showing statistics and rankings.
    
    Args:
        cnx: The database connection object.
        
    Returns:
        None
    """
    try:
        print("\n--- Activity Report ---")
        
        # Total events
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute("SELECT COUNT(*) FROM Events")
        total_events = cur.fetchone()[0]
        
        # Total students
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute("SELECT COUNT(*) FROM Students")
        total_students = cur.fetchone()[0]
        
        # Total participations
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute("SELECT COUNT(*) FROM Participations")
        total_participations = cur.fetchone()[0]
        
        # Total points distributed
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute("SELECT SUM(PointsAwarded) FROM Participations")
        result = cur.fetchone()
        total_points = result[0] if result and result[0] is not None else 0
        
        # House-wise points
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute("SELECT Name, Points FROM Houses ORDER BY Points DESC")
        house_points = cur.fetchall()
        
        # Display report
        print(f"\nTotal Events: {total_events}")
        print(f"Total Students: {total_students}")
        print(f"Total Participations: {total_participations}")
        print(f"Total Points Distributed: {total_points}")
        
        print("\nHouse-wise Points:")
        table = PrettyTable()
        table.field_names = ["House", "Points"]
        table.align = "l"
        table.set_style(TableStyle.SINGLE_BORDER)
        
        for house, points in house_points:
            table.add_row([house, points])
            
        print(table)
        
        # Top 5 participants by points
        print("\nTop 5 Participants:")
        cur = create_database_cursor(cnx)
        if cur is None:
            print("Failed to create database cursor!")
            return
        cur.execute(
            "SELECT s.Name, s.House, s.Points "
            "FROM Students s "
            "ORDER BY s.Points DESC "
            "LIMIT 5"
        )
        top_participants = cur.fetchall()
        
        table = PrettyTable()
        table.field_names = ["Name", "House", "Points"]
        table.align = "l"
        table.set_style(TableStyle.SINGLE_BORDER)
        
        for name, house, points in top_participants:
            table.add_row([name, house, points])
            
        print(table)
        
    except Exception as e:
        print(f"Error generating activity report: {e}")


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
    if cnx is None:
        print("Failed to connect to database!")
        return

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

    if cnx is not None:
        cnx.close()