# pylint: disable=too-many-instance-attributes
"""Model for CPU and DTU metrics."""
from dataclasses import dataclass

@dataclass
class TimeSeries:
    """Template for creating an object to return"""
    aggregation: dict
