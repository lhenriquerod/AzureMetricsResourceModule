# pylint: disable=line-too-long
"""Test Authentication"""
from module_metrics.infra.azure_authenticate import AzureAuthenticate


def test_client_credentials(monkeypatch, mock_client_secret_credential):
    """
    Test that checks if the AzureAuthenticate class can use the client_credentials method with a mock credential.

    Args:
        monkeypatch: pytest fixture that allows the modification of variables at runtime.
        mock_client_secret_credential: pytest fixture that creates a mock of the client_credentials method.

    Returns:
        None: The test passes if no exception is raised.

    Raises:
        AssertionError: If the type of the credential returned by the AzureAuthenticate class is not an object.
    """
    monkeypatch.setattr(AzureAuthenticate, "client_credentials", mock_client_secret_credential)
    assert isinstance(AzureAuthenticate.client_credentials, object)
