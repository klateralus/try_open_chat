from __future__ import annotations
from getpass import getuser
from keyring import set_password, get_password


SERVICE = "open_ai_api_key"


def get_api_key() -> None | str:
    return get_password(SERVICE, getuser())


def set_api_key(key: str) -> None:
    set_password(SERVICE, getuser(), key)
