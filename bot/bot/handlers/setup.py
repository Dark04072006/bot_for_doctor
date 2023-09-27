from .commands import (
    start_command_handler
)

from aiogram import Dispatcher
from aiogram.filters import CommandStart


def setup_handlers(dispatcher: Dispatcher) -> None:

    dispatcher.message.register(
        start_command_handler,
        CommandStart(ignore_case=True)
    )
