"""Create test for validate_interval_metric method."""
from module_metrics.utils.interval_validator import IntervalMetricValidator

def test_valid_interval_metric():
    """
    Tests when the input string is valid.
    """
    interval_validator = IntervalMetricValidator()
    interval = 'PT1M'
    assert interval_validator.validate_interval_metric(interval) == interval

def test_invalid_interval_metric():
    """
    Tests when the input string is invalid.
    """
    interval_validator = IntervalMetricValidator()
    interval = 'PT2H'
    assert interval_validator.validate_interval_metric(interval) is None
