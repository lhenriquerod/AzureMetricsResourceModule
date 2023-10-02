"""Create test for validate_aggregation_metric method"""
from module_metrics.utils.aggregation_validator import AggregationMetricValidator

def test_validate_aggregation_metric():
    """
     Tests whether the validate_aggregation_metric() method of the AggregationMetricValidator class
     returns the string 'Total' when it receives 'Total' as a parameter.
     """
    aggregation = AggregationMetricValidator()
    aggregation_str = 'Total'
    metrics = aggregation.validate_aggregation_metric(aggregation_str)
    assert metrics == aggregation_str

def test_invalid_aggregation_metric():
    """
     Tests whether the validate_aggregation_metric() method of the AggregationMetricValidator class
     returns None when given an invalid string as a parameter.
     """
    aggregation = AggregationMetricValidator()
    aggregation_str = 'Totaly'
    metrics = aggregation.validate_aggregation_metric(aggregation_str)
    assert metrics is None
