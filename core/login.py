"""
Module for handling user authentication and login logic.
"""

from core.exceptions import InvalidUserCredentials

from .utils import connect_to_database, create_database_cursor


def validate_user(username, password):
    """
    Authenticates a user by checking credentials against the database.

    Args:
        username (str): The username string provided by the user.
        password (str): The password string provided by the user.

    Returns:
        tuple[str, str]: A tuple containing (username, role) upon successful validation.

    Raises:
        InvalidUserCredentials: If the username and password do not match any record in the database.
    """
    cnx = connect_to_database()
    cur = create_database_cursor(cnx)
    cur.execute("SELECT * FROM Users;")

    for row in cur:
        if row[1] == username and row[2] == password:
            return (username, row[3])

    raise InvalidUserCredentials()
