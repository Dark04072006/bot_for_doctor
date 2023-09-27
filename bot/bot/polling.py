from .core.telegram import telegram_bot, dispatcher


async def start_polling() -> None:
    await dispatcher.start_polling(telegram_bot)
