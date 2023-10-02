# pylint: disable=line-too-long
"""Create test for validate_date_string method"""
from datetime import datetime
from module_metrics.utils.date_validator import DateValidator

def test_if_len_date_is_greater_than_10():
    """
    Tests when the input string is greater than 10.
    """
    date_validator = DateValidator()
    date_str = '04-20-2023 04:00:00'
    assert date_validator.validate_date_string(date_str) == datetime.strptime(date_str, '%m-%d-%Y %H:%M:%S')

def test_if_len_date_is_less_than_10():
    """
    Tests when the input string is less than 10.
    """
    date_validator = DateValidator()
    date_str = '04-20-2023'
    assert date_validator.validate_date_string(date_str) == datetime.strptime(date_str, '%m-%d-%Y')

def test_if_date_is_not_string():
    """
    Tests when the input is not string.
    """
    date_validator = DateValidator()
    date_str = 2
    assert date_validator.validate_date_string(date_str) is None

def test_valid_year():
    """
    Tests when the input string is valid.
    """
    date_validator = DateValidator()
    date_str = '04-01-2023 00:00:00'
    date = datetime.strptime(date_str, '%m-%d-%Y %H:%M:%S')
    assert date_validator.validate_year(date.year) == 2023

def test_invalid_year():
    """
    Tests when the input string is invalid.
    """
    date_validator = DateValidator()
    date_str = '04-01-2024 00:00:00'
    date = datetime.strptime(date_str, '%m-%d-%Y %H:%M:%S')
    assert date_validator.validate_year(date.year) is None
