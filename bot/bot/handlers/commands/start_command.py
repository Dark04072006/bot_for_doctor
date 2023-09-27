from aiogram.types import Message
from aiogram.utils.i18n import gettext as _


async def start_command_handler(message: Message) -> None:

    await message.answer(
        _('<b>{first_name}</b>, you just sent me /start!').format(
            first_name=message.from_user.first_name
        )
    )
