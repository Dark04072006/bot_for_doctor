from bot.routes import setup_routes
from aiohttp.web import Application

application = Application()
setup_routes(application)
