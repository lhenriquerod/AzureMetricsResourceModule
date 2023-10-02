# pylint: disable=line-too-long
"""test the method to generates the expected error message."""
from module_metrics.utils.exception import Error

def test_exception_error():
    """
    Test that exception_error method generates the expected error message.
    """
    error = Error()
    assert error.exception_error('test_exception_error', 'Error') == "Called Method: test_exception_error(). Error: Error."
