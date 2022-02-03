"""Configarution load module

This module loads the configuration from configuration file.
Provides acess to Config class and config singleton
"""
import json
import sys

from colorama import Fore, init

init(autoreset=True)


class Config:
    """Config class

    This class loads the configuration from configuration file.
    Returns object of Config class.
    """

    def _get(self, group: str, key: str = None) -> str:
        """Get the value of group or key in group

        If value is not present in configuration file, default value is returned.
        If key is not present in neither configuration file nor default file, None is returned.
        """
        if key is None:
            if group in self.config_json:
                return self.config_json[group]
            return ""
        if group in self.config_json and key in self.config_json[group]:
            return self.config_json[group][key]
        return ""

    def __init__(self) -> None:
        """Initialize the Config class"""
        try:
            with open("config/config.json", "r", encoding="utf-8") as config_file:
                self.config_json = json.load(config_file)
        except FileNotFoundError:
            print(f"{Fore.RED}[✗] Configuration file not found. Exiting...")
            sys.exit(1)

        self.servers = self._get("radio", "servers")

    @property
    def debug(self) -> bool:
        """Get the debug mode"""
        return self._get("debug") == "True"

    @property
    def hostname(self) -> str:
        """Get radio hostname"""
        return self._get("radio", "hostname")

    @property
    def port(self) -> str:
        """Get radio port"""
        return self._get("radio", "port")

    @property
    def password(self) -> str:
        """Get icecast password"""
        return self._get("radio", "password")

    @property
    def streams(self) -> str:
        """Get list of streams"""
        return self._get("radio", "streams")

    def reload(self) -> None:
        """Reload the configuration"""
        self.__init__()

    def save(self) -> None:
        """Save the configuration"""
        with open("config/config.json", "w", encoding="utf-8") as config_file:
            json.dump(self.config_json, config_file, indent=4)


config = Config()


def get_config() -> Config:
    """Returns config"""
    return config
