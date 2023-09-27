from os import getenv
from typing import Optional

from .exceptions import MissingEnvVariable


def get_env_var(
        variable_name: str,
        default: Optional[str] = None,
        raise_exception: bool = True
) -> str:

    if not (variable := getenv(variable_name, default)):

        if raise_exception:
            raise MissingEnvVariable(f'<{variable_name}> is missing')

    return variable
