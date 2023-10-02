# pylint: disable=line-too-long,unused-argument,singleton-comparison
"""Create tests for AzureMetricsService methods"""
from module_metrics.services.metrics_services import AzureMetricsService
from module_metrics.entities.metrics import MetricsModel
from module_metrics.entities.time_series import TimeSeries

def test_eligibility_percentil(mock_metric_list):
    """Test the eligibility percentile of a given metric and returns True if the expected value matches.

    Args:
        mock_metric_list: Pytest fixture that mocks the 'MonitorManagementClient' class of the
                          'azure.monitoring.v2018_09_01' module.

    Returns:
        bool: True if the expected value matches, False otherwise.

    """
    azure_metric_service = AzureMetricsService()
    expected = azure_metric_service.eligibility_percentil(metricname='Percentage CPU' ,sub_id='123456789', resource_id="/subscriptions/123456789/resourceGroups/rg-gdms-qa/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTAS301", start_time="05-01-2023 00:00:00", end_time="05-30-2023 00:00:00", interval="PT6H", aggregation="maximum", percentile=95, porcentage=20)

    assert expected == True

def test_peak_eligibility(mock_metric_list):
    """Test the peak eligibility of a given metric and returns True if the expected value matches.

    Args:
        mock_metric_list: Pytest fixture that mocks the 'MonitorManagementClient' class of the
                          'azure.monitoring.v2018_09_01' module.

    Returns:
        bool: True if the expected value matches, False otherwise.

    """
    azure_metric_service = AzureMetricsService()
    expected = azure_metric_service.peak_eligibility('Percentage CPU', sub_id="615e7ca6-1c2c-49d4-b202-c61c03e7eb47", resource_id="/subscriptions/615e7ca6-1c2c-49d4-b202-c61c03e7eb47/resourceGroups/rg-gdms-qa/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTAS301", start_time='04-01-2023 00:00:00', end_time='04-01-2023 23:59:59', interval='PT24H', aggregation="maximum", usage_peak=3)

    assert expected == True

def test_metrics_average(mock_metric_list):
    """Test the average of a given metric and returns the value if the expected value matches.

    Args:
        mock_metric_list: Pytest fixture that mocks the 'MonitorManagementClient' class of the
                          'azure.monitoring.v2018_09_01' module.

    Returns:
        float: The value of the average if the expected value matches.

    """
    azure_metric_service = AzureMetricsService()
    expected = azure_metric_service.metrics_average('Percentage CPU', sub_id="615e7ca6-1c2c-49d4-b202-c61c03e7eb47", resource_id="/subscriptions/615e7ca6-1c2c-49d4-b202-c61c03e7eb47/resourceGroups/rg-gdms-qa/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTAS301", start_time='04-01-2023 00:00:00', end_time='04-01-2023 23:59:59', interval='PT24H', aggregation="maximum")

    assert expected == 56.18

def test_get_metrics_azure(mock_metric_list):
    """Test the get metrics of a given metric and returns a list of metrics if the expected value matches.

    Args:
        mock_metric_list: Pytest fixture that mocks the 'MonitorManagementClient' class of the
                          'azure.monitoring.v2018_09_01' module.

    Returns:
        list: A list of metrics if the expected value matches.

    """
    azure_metric_service = AzureMetricsService()
    expected = azure_metric_service.get_metrics_azure('Percentage CPU', sub_id="615e7ca6-1c2c-49d4-b202-c61c03e7eb47", resource_id="/subscriptions/615e7ca6-1c2c-49d4-b202-c61c03e7eb47/resourceGroups/rg-gdms-qa/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTAS301", start_time='04-01-2023 00:00:00', end_time='04-01-2023 23:59:59', interval='PT24H', aggregation="maximum")

    assert expected == [MetricsModel(metrics=TimeSeries(aggregation={'maximum': 56.18}))]
