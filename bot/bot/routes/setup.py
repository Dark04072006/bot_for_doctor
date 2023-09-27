from .index import (
    index_route
)

from aiohttp.web import Application, RouteTableDef


def setup_routes(application: Application) -> None:
    router = RouteTableDef()
    router.get('/')(index_route)
    application.add_routes(router)
