from .settings import TG_TOKEN, STORAGE

from bot.handlers import setup_handlers
from bot.middlewares import setup_middlewares

import logging
from aiogram.utils.token import TokenValidationError

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

logger = logging.getLogger(__name__)

try:
    telegram_bot = Bot(TG_TOKEN, parse_mode=ParseMode.HTML)
except TokenValidationError:
    logger.fatal('Token is invalid')
    exit(1)

dispatcher = Dispatcher(storage=STORAGE)

setup_handlers(dispatcher)
setup_middlewares(dispatcher)
