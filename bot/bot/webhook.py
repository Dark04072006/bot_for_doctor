from .core.application import application
from .core.telegram import telegram_bot, dispatcher

from .core.settings import (
    WEBHOOK_HOST,
    WEBHOOK_PATH,
    WEBHOOK_PORT
)

from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    setup_application,
)

from aiogram import Bot
from aiohttp.web import run_app


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
    )


async def on_shutdown(bot: Bot) -> None:
    await bot.delete_webhook()
    await bot.session.close()


def start_webhook() -> None:
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    request_handler = SimpleRequestHandler(
        bot=telegram_bot,
        dispatcher=dispatcher
    )

    request_handler.register(application, WEBHOOK_PATH)
    setup_application(application, dispatcher, bot=telegram_bot)

    run_app(application, host='0.0.0.0', port=WEBHOOK_PORT)
