#pylint: disable = too-few-public-methods
"""Module created to generate an error message."""
class Error:
    """Class created to generate an error message."""

    def exception_error(self, method: str, exception: str):
        """Mothod created to generate an error message."""
        called_method = method
        exception_error = exception

        return f"Called Method: {called_method}(). Error: {exception_error}."
