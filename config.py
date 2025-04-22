from configparser import ConfigParser
import os


class ConfigMixin:
    @staticmethod
    def get_config_path():
        def default_config_dir():
            home = os.environ["HOME"]
            return f"{home}/.config/spyk/config.ini"

        return os.environ.get("XDG_CONFIG_HOME", default_config_dir())

    @property
    def config(self):
        config = ConfigParser()
        config.read(self.get_config_path())
        return config

    def goto_vault(self):
        os.chdir(self.vault_path)

    def __init__(self):
        self.vault_path = self.config["vault"]["path"]
        self.goto_vault()
