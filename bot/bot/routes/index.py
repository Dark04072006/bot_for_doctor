from bot.core.telegram import telegram_bot
from aiohttp.web import Request, Response, json_response


async def index_route(request: Request) -> Response:
    me = await telegram_bot.get_me()
    return json_response(me.model_dump())
