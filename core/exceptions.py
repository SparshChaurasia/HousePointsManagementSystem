"""
Custom exception classes for specific application error scenarios.
"""


class InvalidInputLength(Exception):
    """
    Raised when an input value does not meet the required length.
    """

    def __init__(self):
        super().__init__("Input does not meet the required length!")


class InputLengthExceeded(Exception):
    """
    Raised when an input value exceeds the maximum allowed length.
    """

    def __init__(self):
        super().__init__("Input exceeds the maximum allowed length!")


class InvalidDateFormat(Exception):
    """
    Raised when a date string is not in the expected format.
    """

    def __init__(self):
        super().__init__("Please enter date in the valid format!")


class InvalidUserCredentials(Exception):
    """
    Raised when user credentials are invalid.
    """
    
    def __init__(self):
        super().__init__("Invalid user credentials!")
