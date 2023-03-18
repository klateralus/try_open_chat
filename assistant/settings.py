from pathlib import Path
from pickle import load, dump, DEFAULT_PROTOCOL
from getpass import getuser


class Settings(object):
    """ This is a very simple settings class, just for previewing of the AI Assistant
    """
    SETTINGS_SUB_PATH = r"settings\tools.pickle"

    @staticmethod
    def _get_file_path() -> Path:
        """ Method returns path to the file with settings
        """
        return Path().joinpath(Settings.SETTINGS_SUB_PATH).absolute()

    @staticmethod
    def _retrieve_settings() -> dict:
        """ Method returns user specific settings stored in a file
        """
        path = Settings._get_file_path()
        if not path.exists():
            return dict()

        with open(str(path), "rb") as pickle_file:
            return load(pickle_file)

    @staticmethod
    def _store_settings(settings: dict):
        path = Settings._get_file_path()
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        with open(str(path), "wb") as pickle_file:
            dump(settings, pickle_file, DEFAULT_PROTOCOL)

    @staticmethod
    def get_tool_settings(tool_ids: tuple) -> dict:
        settings = Settings._retrieve_settings()

        user_key = str(getuser())
        user_settings = settings.get(user_key, dict())

        tool_key = "".join(tool_ids)
        tool_settings = user_settings.get(tool_key, dict())
        return tool_settings

    @staticmethod
    def set_tool_settings(tool_ids: tuple, new_settings: dict):
        settings = Settings._retrieve_settings()

        user_key = str(getuser())
        user_settings = settings.get(user_key, dict())

        tool_key = "".join(tool_ids)
        user_settings[tool_key] = new_settings

        settings[user_key] = user_settings

        Settings._store_settings(settings)






