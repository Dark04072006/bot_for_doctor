from bot.utils import get_env_var

import logging.config
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent.parent

I18N_DOMAIN = 'bot'
I18N_DEFAULT_LANGUAGE = 'en'
I18N_LOCALES_DIR = BASE_DIR / 'locales'

logging.config.fileConfig(BASE_DIR / 'logging.conf')

STORAGE = None
TG_TOKEN = get_env_var('TG_TOKEN')

WEBHOOK_HOST = get_env_var('WEBHOOK_HOST')
WEBHOOK_PATH = get_env_var('WEBHOOK_PATH', '/webhook/')
WEBHOOK_PORT = get_env_var('WEBHOOK_PORT', 3001)

REDIS_HOST = None
REDIS_PORT = None
REDIS_DB = None
REDIS_PASSWORD = None
