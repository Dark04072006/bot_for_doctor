from aiogram import Dispatcher
from .i18n_middleware import i18n_middleware


def setup_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.update.outer_middleware(i18n_middleware)
