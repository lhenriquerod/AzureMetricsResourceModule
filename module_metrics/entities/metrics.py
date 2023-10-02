# pylint: disable=too-many-instance-attributes
"""Model for CPU Metrics data."""

from dataclasses import dataclass


@dataclass
class MetricsModel:
    """Template for creating an object to return"""
    metrics: list
