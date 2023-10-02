# pylint: disable=line-too-long,unused-argument
"""Create test for get_metrics method"""
from module_metrics.entities.time_series import TimeSeries
from module_metrics.entities.metrics import MetricsModel
from module_metrics.infra.azure_metrics import AzureMetrics


def test_get_metrics(mock_metric_list):
    """
    Test the 'azure_metrics_list' function of the AzureMetrics class.

    Args:
        mock_metric_list: Pytest fixture that mocks the 'MonitorManagementClient' class of the
                          'azure.monitoring.v2018_09_01' module.

    Returns:
        None. Raises AssertionError if the expected output is not obtained.
    """
    azure_metrics = AzureMetrics()
    expected = azure_metrics.azure_metrics_list(metricname='Percentage CPU' ,sub_id='123456789', resource_id="/subscriptions/123456789/resourceGroups/rg-gdms-qa/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTAS301", start_time="05-01-2023 00:00:00", end_time="05-30-2023 00:00:00", interval="PT6H", aggregation="maximum")

    assert expected == [MetricsModel(metrics=TimeSeries(aggregation={'maximum': 56.18}))]
