# pylint: disable=too-few-public-methods,line-too-long

"""Credentials authentication"""
from azure.identity import ClientSecretCredential
from module_metrics.infra.config import Config

class AzureAuthenticate:
    """
    A class that handles Azure authentication using a client secret.

    Attributes:
        __config (Config): An instance of the Config class that stores the necessary Azure credentials.

    Methods:
        client_credentials(): Returns a ClientSecretCredential object, which can be used to authenticate Azure services
        using a client secret.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the AzureAuthenticate class and creates an instance of the Config class to store
        the necessary Azure credentials.
        """
        self.__config = Config()


    def client_credentials(self):
        """
        Returns a ClientSecretCredential object, which can be used to authenticate Azure services using a client secret.

        Returns:
            ClientSecretCredential: A ClientSecretCredential object that contains the tenant ID, client ID, and client
            secret necessary for Azure authentication.
        """
        return ClientSecretCredential(
            tenant_id= self.__config.tenant_id,
            client_id= self.__config.client_id,
            client_secret= self.__config.client_secret
        )
