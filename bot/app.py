import logging
from bot import start_webhook

from argparse import ArgumentParser
from aiogram.exceptions import TelegramUnauthorizedError

logger = logging.getLogger(__name__)

parser = ArgumentParser(
    'Telegram Bot',
    description='Telegram Bot template',
    epilog='Webhook Server requires additional environment variables'
)


if __name__ == '__main__':

    try:
        start_webhook()
    except TelegramUnauthorizedError:
        logger.fatal('Token is wrong')
        exit(1)
