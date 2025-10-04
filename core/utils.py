import os

import mysql.connector
from mysql.connector import errorcode
from prettytable import TableStyle, from_db_cursor


def clear_screen():
    """
    Clears the terminal screen

    Args:
        None

    Returns:
        None
    """

    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")


def print_queryset(cur):
    table = from_db_cursor(cur)
    table.align = "l"
    table.set_style(TableStyle.SINGLE_BORDER)
    print(table)


def int_input(message, rng=None):
    try:
        print(message)
        ch = int(input(">>> "))

        if not rng:
            return ch

        if ch >= rng[0] and ch <= rng[1]:
            return ch
        else:
            print("Please enter a valid choice / number")
            return -1
    except:
        print("Please enter a valid choice / number")
        return -1


def char_input(message, length=-1, max_length=-1):
    try:
        text = input(message)
    except Exception:
        print("Please enter a valid string!")
        return -1
    if length > 0:
        if len(text) == length:
            return text
        else:
            print(f"Please enter a string of length {length} characters!")
            return -1
    elif max_length > 0:
        if len(text) <= max_length:
            return text
        else:
            print(f"Please enter a string of maximum length of {length} characters!")
            return -1


def input_from_choice(choices):
    i = 1
    for choice in choices:
        print(f"{i}. {choice}")
    ch = int_input(">>> ", (1, len(choices)))

    return choices[ch]


def connect_to_database():
    """
    Creates a connection to database and returns the database connection object

    Args:
        None

    Returns:
        mysql.connector.MySQLConnection: Database connection object
    """

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
