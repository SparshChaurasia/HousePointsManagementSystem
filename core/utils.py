"""
Utility module containing helper functions for common tasks like console management, user input handling, database connectivity, and data display.

This module simplifies terminal interaction, robust input validation, and standard database operations across the application.
"""

import os

import mysql.connector
from mysql.connector import errorcode
from prettytable import TableStyle, from_db_cursor

from core.exceptions import *


def clear_screen():
    """
    Clears the terminal screen using OS-specific commands.
    """

    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")


def print_queryset(cur):
    """
    Prints the results of a database query using a formatted table.

    Args:
        cur: The database cursor object containing the query results.
    """

    table = from_db_cursor(cur)
    table.align = "l"
    table.set_style(TableStyle.SINGLE_BORDER)
    print(table)


def int_input(message=None, rng=None):
    """
    Prompts the user for integer input and validates it against the given range (optional).

    Args:
        message (str, optional): The prompt message to display to the user.
        rng (tuple[int, int], optional): A tuple (min, max) defining the acceptable range (inclusive).

    Returns:
        int: The validated integer input, or -1 if the input is invalid or falls outside the specified range.
    """

    try:
        if not None:
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
    """
    Prompts the user for string input and validates its length.

    Args:
        message (str): The prompt message to display to the user.
        length (int, optional): The exact required length of the string. Defaults to -1 (no exact length check).
        max_length (int, optional): The maximum allowed length of the string. Defaults to -1 (no max length check).

    Returns:
        str: The validated string input.

    Raises:
        InvalidInputLength: If an exact `length` is specified and not met.
        InputLengthExceeded: If `max_length` is specified and exceeded.
    """

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
            raise InvalidInputLength

    elif max_length > 0:
        if len(text) <= max_length:
            return text
        else:
            print(
                f"Please enter a string of maximum length of {max_length} characters!"
            )
            raise InputLengthExceeded


def date_input(message):
    """
    Prompts the user for date input and validates it against the 'YYYY-MM-DD' format.

    Args:
        message (str): The prompt message to display to the user.

    Returns:
        str: The validated date string in 'YYYY-MM-DD' format.

    Raises:
        InvalidDateFormat: If the format is incorrect or any part (Y, M, D) is not a valid integer.
    """

    text = input(message)
    lst = text.split("-")

    # Check if the format of the date is correct
    if not (len(lst[0]) == 4 and len(lst[1]) == 2 and len(lst[2])) == 2:
        raise InvalidDateFormat

    try:
        # Check if the date, month and year part is number
        y = int(lst[0])
        m = int(lst[1])
        d = int(lst[2])
    except Exception:
        raise InvalidDateFormat

    return text


def input_from_choice(message, choices):
    """
    Displays a numbered list of choices to the user and returns the selected item.

    Args:
        message (str): The prompt message to display before the list of choices.
        choices (list[str]): A list of strings representing the available options.

    Returns:
        str: The selected item from the `choices` list.

    Raises:
        Exception: If the integer input is invalid (returns -1 from int_input).
    """

    print(message)
    i = 1
    for choice in choices:
        print(f"{i}. {choice}")
        i += 1
    ch = int_input(rng=(1, len(choices)))

    if ch == -1:
        raise Exception

    return choices[ch - 1]


def connect_to_database():
    """
    Establishes and returns a connection object to the MySQL database.

    Connection details (user, password, host, database) are hardcoded.

    Returns:
        mysql.connector.MySQLConnection or None: The database connection object if successful, or None if a connection error occurs.
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
    """
    Creates and returns a database cursor object from an active connection.

    Args:
        cnx (mysql.connector.MySQLConnection): The active database connection object.

    Returns:
        mysql.connector.cursor.MySQLCursor: The database cursor object.

    Raises:
        mysql.connector.Error: If an error occurs while creating the cursor.
    """

    try:
        cur = cnx.cursor()

        return cur
    except mysql.connector.Error as err:
        print("Error in creating cursor")
        print(err)
