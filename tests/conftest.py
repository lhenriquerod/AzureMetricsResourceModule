# pylint: disable=line-too-long,unused-argument
"""Create mocks and fixtures for tests"""
from unittest.mock import MagicMock
from types import SimpleNamespace
from pytest import fixture
import module_metrics.infra.azure_metrics as mock_azure_metrics


@fixture(autouse=True)
def mock_env_var(monkeypatch):
    """
    Fixture that sets environment variables for Azure authentication to be used in tests.

    Args:
        monkeypatch: pytest fixture that provides a way to temporarily replace or modify
                     attributes, functions or classes.
    """
    monkeypatch.setenv("AZURE_TENANT_ID", "tenant")
    monkeypatch.setenv("AZURE_CLIENT_ID", "client")
    monkeypatch.setenv("AZURE_CLIENT_SECRET", "secret")

@fixture
def mock_client_secret_credential():
    """
    Fixture that returns a mock of the Azure Identity Client's `ClientSecretCredential`
    class for testing purposes.

    Returns:
        A mock of the `ClientSecretCredential` class.
    """
    mock_credential = MagicMock()
    mock_credential.return_value = mock_credential
    return mock_credential


@fixture
def mock_metric_list(monkeypatch):
    """Fixture that returns a mock of the Azure MonitorManagementClient's `metrics.list` method for testing purposes.

    Args:
        monkeypatch: pytest fixture that provides a way to temporarily replace or modify attributes, functions or classes.
    Returns:
        A mock of the `MonitorManagementClient` class.
    """
    def mock_metrics(*args):
        mock_monitor_management_client = MagicMock()
        mock_client_metrics = MagicMock()
        mock_monitor_management_client.metrics = mock_client_metrics

        maximum = {'maximum': 56.18}
        maximum = SimpleNamespace(**maximum)

        metric_list = MagicMock()
        metric_list.value = [MagicMock()]
        metric_list.value[0].timeseries = [MagicMock()]
        metric_list.value[0].timeseries[0].data = [MagicMock()]
        metric_list.value[0].timeseries[0].data.append(maximum)
        metric_list.value[0].timeseries[0].data.pop(0)

        def mock_list(*args, **Kwargs):
            return metric_list

        mock_client_metrics.list = mock_list

        return mock_monitor_management_client

    monkeypatch.setattr(mock_azure_metrics, "MonitorManagementClient", mock_metrics)
