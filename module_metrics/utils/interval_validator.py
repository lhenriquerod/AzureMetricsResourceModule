# pylint: disable=line-too-long
# pylint: disable=no-else-return
# pylint: disable=too-few-public-methods
"""Validate if a time interval is valid or not"""

class IntervalMetricValidator:
    """
    Class to validate if a time interval is valid or not.
    """

    def validate_interval_metric(self, interval: str):
        """
        Validates whether a time interval is valid or not.

        Args:
            interval(str): The time interval to validate.

        returns:
            str: The validated time interval, if valid.

        Raises:
            SystemExit: If the time interval is not valid.
        """
        if interval in {
            'PT1M',
            'PT5M',
            'PT15M',
            'PT30M',
            'PT1H',
            'PT6H',
            'PT12H',
            'PT24H',
        }:
            return interval

        print('Invalid interval. Valid intervals:"PT1M" (1 minute),"PT5M" (5 minutes),"PT15M" (15 minutes),"PT30M" (30 minutes),"PT1H" (1 hour),"PT6H"(6 hours)"PT12H", (12 hours)"PT24H" (24 hours)')
        return None
