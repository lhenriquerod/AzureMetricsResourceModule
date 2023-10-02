# pylint: disable=line-too-long,too-many-arguments,unsubscriptable-object,too-many-locals,broad-exception-caught,inconsistent-return-statements
"""Class to get metrics"""
import pandas as pd
from module_metrics.infra.azure_metrics import AzureMetrics
from module_metrics.utils.date_validator import DateValidator
from module_metrics.utils.interval_validator import IntervalMetricValidator
from module_metrics.utils.aggregation_validator import AggregationMetricValidator
from module_metrics.utils.exception import Error


class AzureMetricsService:
    """
    A class that provides methods for retrieving metrics for a given Azure resource using Azure Monitor Management Client.
    """

    def __init__(self):
        """
        Initializes the AzureMetricsService class with an instance of the AzureMetrics class.
        """
        self.__azure_metrics = AzureMetrics()
        self.__error = Error()


    def eligibility_percentile(self, metricname: str, sub_id:str, resource_id: str, start_time:str, end_time:str, interval:str, aggregation:str, percentile=95, porcentage=20):
        """
        Retrieves the eligibility percentil of a given Azure resource based on the maximum value of the specified metric.

        Args:
            metricname (str): The name of the metric to retrieve.
            sub_id (str): The subscription ID of the Azure resource.
            resource_id (str): The ID of the Azure resource.
            start_time (str): The start time for the metric query in ISO 8601 format.
            end_time (str): The end time for the metric query in ISO 8601 format.
            interval (str): The interval for the metric query, in duration format.
            aggregation (str): The aggregation type for the metric query.
            percentile (float, optional): The percentile to calculate for the maximum metric value. Defaults to 95.
            porcentage (float, optional): The percentage to compare against the percentile value. Defaults to 20.

        Returns:
            bool: True if the percentile value is greater than or equal to the specified percentage, False otherwise.
        """

        metrics_azure = self.__azure_metrics.azure_metrics_list(metricname, sub_id, resource_id, start_time, end_time, interval, aggregation)
        metrics_list = []

        try:
            for metric in metrics_azure:
                metrics = metric.metrics.aggregation['maximum']
                if metrics is None:
                    metrics = 0
                metrics_list.append(metrics)
            metrics_list = pd.DataFrame(metrics_list)
            metrics_list = metrics_list.dropna()
            percentile = percentile/100
            percentile_value = metrics_list.quantile(q=percentile)

            return percentile_value[0] >= porcentage
        except Exception as exception:
            print(self.__error.exception_error('eligibility_percentil', exception))

    def peak_eligibility(self, metricname: str, sub_id:str, resource_id: str, start_time:str, end_time:str, interval:str, aggregation:str, usage_peak: int, percentage= 20):
        """
        Determines if the given Azure resource has exceeded the specified usage peak percentage.

        Args:
            metricname (str): The name of the metric to retrieve.
            sub_id (str): The subscription ID of the Azure resource.
            resource_id (str): The ID of the Azure resource.
            start_time (str): The start time for the metric query in ISO 8601 format.
            end_time (str): The end time for the metric query in ISO 8601 format.
            interval (str): The interval for the metric query, in duration format.
            aggregation (str): The aggregation type for the metric query.
            usage_peak (int): The maximum number of times the metric should exceed the specified percentage.
            percentage (float): The percentage value to use as the usage peak threshold. Default 20.

        Returns:
            bool: True if the number of times the metric exceeded the specified percentage is less than the usage peak value, False otherwise.
        """
        metrics_azure = self.__azure_metrics.azure_metrics_list(metricname, sub_id, resource_id, start_time, end_time, interval, aggregation)
        metrics_list = []

        try:
            for metric in metrics_azure:
                metrics = metric.metrics.aggregation[aggregation]
                if metrics is None:
                    metrics = 0
                metrics_list.append(metrics)
            metrics_list = pd.DataFrame(metrics_list)
            metrics_list = metrics_list.dropna()
            metrics_list = metrics_list.rename(columns={0: aggregation})
            top_usage = metrics_list[metrics_list[aggregation] >= percentage].nlargest(usage_peak, aggregation)

            return len(top_usage[aggregation]) < usage_peak
        except Exception as exception:
            print(self.__error.exception_error('peak_eligibility', exception))


    def metrics_average(self, metricname: str, sub_id:str, resource_id: str, start_time:str, end_time:str, interval:str, aggregation:str):
        """
        Retrieves the average value of a given metric for a specified Azure resource.

        Args:
            metricname (str): The name of the metric to retrieve.
            sub_id (str): The subscription ID of the Azure resource.
            resource_id (str): The ID of the Azure resource.
            start_time (str): The start time for the metric query in ISO 8601 format.
            end_time (str): The end time for the metric query in ISO 8601 format.
            interval (str): The interval for the metric query, in duration format.
            aggregation (str): The aggregation type for the metric query.

        Returns:
            float: The average value of the specified metric for the Azure resource.
        """
        metrics_azure = self.__azure_metrics.azure_metrics_list(metricname, sub_id, resource_id, start_time, end_time, interval, aggregation)
        metrics_list = []

        try:
            for metric in metrics_azure:
                metrics = metric.metrics.aggregation['maximum']
                if metrics is None:
                    metrics = 0
                metrics_list.append(metrics)
            metrics_list = pd.DataFrame(metrics_list)
            metrics_list = metrics_list.dropna()
            return metrics_list[0].mean()
        except Exception as exception:
            print(self.__error.exception_error('metrics_average', exception))


    def get_metrics_azure(self, metricname: str, sub_id:str, resource_id: str, start_time:str, end_time:str, interval:str, aggregation:str):
        """
        Retrieves a list of metric values for a specified Azure resource.

        Args:
            metricname (str): The name of the metric to retrieve.
            sub_id (str): The subscription ID of the Azure resource.
            resource_id (str): The ID of the Azure resource.
            start_time (str): The start time for the metric query in ISO 8601 format.
            end_time (str): The end time for the metric query in ISO 8601 format.
            interval (str): The interval for the metric query, in duration format.
            aggregation (str): The aggregation type for the metric query.

        Returns:
            list: A list of metric values for the specified Azure resource.
        """
        date_converter = DateValidator()
        interval_validator = IntervalMetricValidator()
        aggregation_validator = AggregationMetricValidator()

        start_time_str = date_converter.validate_date_string(start_time)
        end_time_str = date_converter.validate_date_string(end_time)
        interval_str = interval_validator.validate_interval_metric(interval)
        aggregation_str = aggregation_validator.validate_aggregation_metric(aggregation)

        try:

            if start_time < end_time:
                return self.__azure_metrics.azure_metrics_list(metricname, sub_id, resource_id, start_time_str, end_time_str, interval_str, aggregation_str)

            print("ERROR: The start_time should be less than the end_time.")
            return None

        except Exception as exception:
            print(self.__error.exception_error('get_metrics_azure', exception))
