# pylint: disable=trailing-whitespace
""" Config class """
import os
import sys
from dynaconf import Dynaconf, Validator, ValidationError


class Config:
    """A class that handles the configuration settings for an Azure application.

    Attributes:
        tenant_id (str): The tenant ID used for authentication with Azure.
        client_id (str): The client ID used for authentication with Azure.
        client_secret (str): The client secret used for authentication with Azure.

    Raises:
        ValidationError: If the configuration settings are not valid.

    """

    def __init__(self) -> None:
        """
        Initializes the Config object by setting up the configuration settings and validating them.
        """
        self.__prefix = "AZURE"
        self.__settingsfile = [
            "settings.toml",
            ".secrets.toml",
        ]
        self.__settings = Dynaconf(
            envvar_prefix=self.__prefix,
            root_path=os.path.dirname(__file__),
            settings_files=self.__settingsfile,
        )

        self.__settings.validators.register(
            Validator(
                "TENANT_ID",
                "CLIENT_ID",
                "CLIENT_SECRET",
                must_exist=True,
            ),
        )
        try:
            self.__settings.validators.validate()
        except ValidationError as error_msg:
            print(f"Error validating config : {str(error_msg)}")
            sys.exit(10)

    @property
    def tenant_id(self) -> str:
        """Returns tenant_id"""
        return self.__settings.TENANT_ID

    @property
    def client_id(self) -> str:
        """Returns client_id"""
        return self.__settings.CLIENT_ID

    @property
    def client_secret(self) -> str:
        """Returns client_secret"""
        return self.__settings.CLIENT_SECRET
    