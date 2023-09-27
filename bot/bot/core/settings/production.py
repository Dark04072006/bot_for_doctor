from .common import *
from bot.utils import get_env_var

from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage

REDIS_HOST = get_env_var('REDIS_HOST')
REDIS_PORT = get_env_var('REDIS_PORT', 6379)
REDIS_DB = get_env_var('REDIS_DB', 0)
REDIS_PASSWORD = get_env_var('REDIS_PASSWORD', None, raise_exception=False)

STORAGE = RedisStorage(Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    password=REDIS_PASSWORD
))
