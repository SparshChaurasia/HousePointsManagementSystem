"""
Utility module for console management, user input handling, database connectivity, and data display.
"""

import os

import mysql.connector
from mysql.connector import errorcode
from prettytable import TableStyle, from_db_cursor
from dotenv import load_dotenv

from core.exceptions import *

# Load environment variables from .env file
load_dotenv()


def clear_screen():
    """Clears the terminal screen using OS-specific commands."""
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")


def print_queryset(cur):
    """
    Prints database query results in a formatted table.
    
    Args:
        cur: Database cursor containing query results.
    """
    table = from_db_cursor(cur)
    if table is not None:
        table.align = "l"
        table.set_style(TableStyle.SINGLE_BORDER)
        print(table)


def int_input(message=None, rng=None):
    """
    Gets integer input from user with optional range validation.
    
    Args:
        message (str, optional): Prompt message to display.
        rng (tuple[int, int], optional): Acceptable range (min, max).
        
    Returns:
        int: Validated integer input.
        
    Raises:
        InvalidInputError: When input is not a valid integer.
        InputRangeError: When input is outside the specified range.
    """
    try:
        if message is not None:
            ch = int(input(message))
        else:
            ch = int(input(">>> "))

        if rng is None:
            return ch

        if rng[0] <= ch <= rng[1]:
            return ch
        else:
            raise InputRangeError()
    except ValueError:
        raise InvalidInputError()


def char_input(message, length=None, max_length=None):
    """
    Gets string input from user with length validation.
    
    Args:
        message (str): Prompt message to display.
        length (int, optional): Exact required length. Defaults to None.
        max_length (int, optional): Maximum allowed length. Defaults to None.
        
    Returns:
        str: Validated string input.
        
    Raises:
        InvalidInputLength: When exact length requirement not met.
        InputLengthExceeded: When maximum length exceeded.
        InvalidInputError: When input cannot be processed or user interrupts input.
    """
    try:
        text = input(message)
    except KeyboardInterrupt:
        raise InvalidInputError()
    except Exception:
        raise InvalidInputError()

    if length is not None:
        if len(text) == length:
            return text
        else:
            raise InvalidInputLength()

    elif max_length is not None:
        if len(text) <= max_length:
            return text
        else:
            raise InputLengthExceeded()
    
    return text


def date_input(message):
    """
    Gets date input from user in YYYY-MM-DD format.
    
    Args:
        message (str): Prompt message to display.
        
    Returns:
        str: Validated date string in YYYY-MM-DD format.
        
    Raises:
        InvalidDateFormat: When format is incorrect or values are not valid numbers.
    """
    text = input(message)
    lst = text.split("-")

    # Check if the format of the date is correct
    if not (len(lst[0]) == 4 and len(lst[1]) == 2 and len(lst[2]) == 2):
        raise InvalidDateFormat()

    try:
        # Check if the date, month and year part is number
        y = int(lst[0])
        m = int(lst[1])
        d = int(lst[2])
    except Exception:
        raise InvalidDateFormat()

    return text


def input_from_choice(message, choices):
    """
    Displays choices and returns user selection.
    
    Args:
        message (str): Prompt message to display.
        choices (list[str]): Available options.
        
    Returns:
        str: Selected item from choices.
        
    Raises:
        InvalidInputError: When input is not a valid integer or out of range.
    """
    print(message)
    i = 1
    for choice in choices:
        print(f"{i}. {choice}")
        i += 1
    try:
        ch = int_input(rng=(1, len(choices)))
    except Exception:
        raise InvalidInputError()

    return choices[ch - 1]


def connect_to_database():
    """
    Establishes connection to MySQL database using credentials from .env file.
    
    Returns:
        mysql.connector.MySQLConnection: Database connection object.
        
    Raises:
        DatabaseConnectionError: When database connection fails.
    """
    try:
        cnx = mysql.connector.connect(
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "tiger"),
            host="127.0.0.1",
            database="HousePointsManagementSystem",
        )

        return cnx
    except mysql.connector.Error as err:
        raise DatabaseConnectionError()


def create_database_cursor(cnx):
    """
    Creates database cursor from connection.
    
    Args:
        cnx (mysql.connector.MySQLConnection): Active database connection.
        
    Returns:
        mysql.connector.cursor.MySQLCursor: Database cursor object.
        
    Raises:
        CursorError: When cursor creation fails.
    """
    try:
        cur = cnx.cursor()

        return cur
    except mysql.connector.Error as err:
        raise CursorError()