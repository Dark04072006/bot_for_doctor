from os import environ

MODE = environ.get('BOT_MODE', 'production')

if MODE == 'development':
    from .development import *

elif MODE == 'production':
    from .production import *
