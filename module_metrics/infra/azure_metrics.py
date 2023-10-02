# pylint: disable=line-too-long,too-many-arguments,too-many-locals,too-few-public-methods,broad-exception-caught,inconsistent-return-statements
"""Provides a wrapper around Azure's Monitor Management Client to retrieve metrics for a given Azure resource."""
from azure.mgmt.monitor import MonitorManagementClient
from module_metrics.infra.azure_authenticate import AzureAuthenticate
from module_metrics.entities.time_series import TimeSeries
from module_metrics.entities.metrics import MetricsModel
from module_metrics.utils.exception import Error


class AzureMetrics:
    """
    Provides a wrapper around Azure's Monitor Management Client to retrieve metrics for a given Azure resource.
    """

    def __init__(self):
        """
        Initializes a new instance of the AzureMetrics class.
        """
        self.__credential = AzureAuthenticate()
        self.__error = Error()

    def azure_metrics_list(self, metricname, sub_id, resource_id: str, start_time, end_time, interval, aggregation):
        """
        Retrieves metrics for a given Azure resource.

        Args:
            metricname (str): The name of the metric.
            sub_id (str): The subscription ID.
            resource_id (str): The resource ID.
            start_time (str): The start time in UTC format.
            end_time (str): The end time in UTC format.
            interval (str): The interval for the metric in minutes.
            aggregation (str): The aggregation function to apply to the metric.

        Returns:
            A list of MetricsModel objects containing the retrieved metrics.
        """

        client = MonitorManagementClient(self.__credential.client_credentials(), sub_id)

        metrics_variable = client.metrics.list(
            resource_uri=resource_id,
            timespan=f"{start_time}/{end_time}",
            interval=interval,
            metricnames=metricname,
            aggregation= aggregation
        )
        metric_data = []
        metric_attrs = {
            'maximum': 'maximum',
            'minimum': 'minimum',
            'average': 'average',
            'count': 'count',
            'total': 'total',
            'sum': 'sum',
            'last': 'last'
        }
        aggregation_key = aggregation.lower()

        try:
            for metric_value in metrics_variable.value[0].timeseries[0].data:

                metric_dict = TimeSeries({
                    metric_attrs[aggregation_key]: getattr(metric_value, metric_attrs[aggregation_key])
                })

                metric_data.append(metric_dict)

            return [
                MetricsModel(item) for item in metric_data
            ]
        except Exception as exception:
            print(self.__error.exception_error('azure_metrics_list', exception))
