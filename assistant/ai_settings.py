# base modules
from pathlib import Path
from json import load
# tool modules
from .settings import Settings

TOOL_TUPLE = ("open_ai", "0", "assistant")
TEMPERATURE = "temperature"
MODEL = "model_name"
TOKENS = "tokens"
BEHAVIOR = "behavior"


def _get_default_settings() -> dict:
    path = Path(__file__).parent.joinpath("default/settings.json")
    with path.open() as file_object:
        return load(file_object)


def _get_default_temperature() -> float:
    return _get_default_settings().get(TEMPERATURE, 1.0)


def _get_default_model() -> str:
    return _get_default_settings().get(MODEL, "gpt-3.5-turbo")


def _get_default_tokens() -> int:
    return _get_default_settings().get(TOKENS, 4096)


def _get_default_behavior() -> str:
    return _get_default_settings().get(BEHAVIOR, "You're a charismatic intellectual who provides interesting answers")


def _settings() -> dict:
    return Settings.get_tool_settings(TOOL_TUPLE)


def _set_settings(value: dict) -> None:
    Settings.set_tool_settings(TOOL_TUPLE, value)


def get_temperature() -> float:
    default = _get_default_temperature()
    return _settings().get(TEMPERATURE, default)


def get_model() -> str:
    # hardcoded chat gpt model
    return _get_default_model()


def get_tokens() -> int:
    default = _get_default_tokens()
    return _settings().get(TOKENS, default)


def get_behavior() -> str:
    default = _get_default_behavior()
    return _settings().get(BEHAVIOR, default)


def set_temperature(value: float) -> None:
    settings = _settings()
    settings[TEMPERATURE] = value
    _set_settings(settings)


def set_model(value: str) -> None:
    settings = _settings()
    settings[MODEL] = value
    _set_settings(settings)


def set_tokens(value: int) -> None:
    settings = _settings()
    settings[TOKENS] = value
    _set_settings(settings)


def set_behavior(value: str) -> None:
    settings = _settings()
    settings[BEHAVIOR] = value
    _set_settings(settings)
