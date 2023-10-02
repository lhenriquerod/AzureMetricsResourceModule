# pylint: disable=line-too-long,no-else-return,chained-comparison,too-few-public-methods,broad-except,inconsistent-return-statements
"""Validate date strings"""
from datetime import datetime
from module_metrics.utils.exception import Error


class DateValidator:
    """A class for validating date strings."""
    def __init__(self):
        self.__error = Error()

    def validate_date_string(self, date_str: str):  # sourcery skip: extract-method
        """
        Validate a date string in the format MM/DD/YYYY HH:MM:SS or MM/DD/YYYY.

        Args:
        - date_str (str): The date string to be validated.

        Returns:
        - datetime.datetime: A datetime object representing the validated date string.

        Raises:
        - Exception: If the input is not a string or has an invalid format.
        - SystemExit: If the year, month, day, hour, minute, or second of the date string is invalid.

        """
        if not isinstance(date_str, str):
            return None
        if len(date_str) > 10:
            try:
                date = datetime.strptime(date_str, '%m-%d-%Y %H:%M:%S')

                year = self.validate_year(date.year)
                date_string = f"{date.month}-{date.day}-{year} {date.hour}:{date.minute}:{date.second}"

                return datetime.strptime(date_string, '%m-%d-%Y %H:%M:%S')
            except Exception as exception:
                print(self.__error.exception_error('validate_date_string', exception))

        else:
            try:
                date = datetime.strptime(date_str, '%m-%d-%Y')

                year = self.validate_year(date.year)
                date_string = f"{date.month}-{date.day}-{year}"

                return datetime.strptime(date_string, '%m-%d-%Y')
            except Exception as exception:
                print(self.__error.exception_error('validate_date_string', exception))

    def validate_year(self, year):
        """
        Validate a year.

        Args:
        - year (int): The year to be validated.

        Returns:
        - int: The validated year.

        Raises:
        - SystemExit: If the year is not between 2000 and 2023.

        """

        if year <= 2023 and year >= 2000:
            return year

        print("Invalid year. Must be between 2000 and 2023.")
        return None
