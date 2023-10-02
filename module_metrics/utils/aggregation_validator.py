# pylint: disable=line-too-long
# pylint: disable=no-else-return
# pylint: disable=too-few-public-methods
"""Validate if an aggregation metric is valid or not."""

class AggregationMetricValidator:
    """
    Class to validate if an aggregation metric is valid or not.
    """

    def validate_aggregation_metric(self, aggregation: str):
        """"
        Validates whether an aggregation metric is valid or not.

        Args:
            aggregation (str): The aggregation metric to be validated.

        returns:
            str: The validated aggregation metric, if valid.

         Raises:
            SystemExit: If the aggregation metric is not valid.
        """

        if aggregation in {'Average', 'average', 'Count', 'count', 'Maximum', 'maximum', 'Minimum', 'minimum', 'Total', 'total', 'Sum', 'sum', 'Last', 'last'}:
            return aggregation

        print("Invalid Aggregation. Valid aggregations: 'Average', 'average', 'Count', 'count', 'Maximum', 'maximum', 'Minimum', 'minimum', 'Total', 'total', 'Sum', 'sum', 'Last', 'last'")
        return None
            