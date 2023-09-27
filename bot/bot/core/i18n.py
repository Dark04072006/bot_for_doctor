from .settings import (
    I18N_DOMAIN,
    I18N_DEFAULT_LANGUAGE,
    I18N_LOCALES_DIR
)

from aiogram.utils.i18n import I18n

i18n = I18n(
    path=I18N_LOCALES_DIR,
    default_locale=I18N_DEFAULT_LANGUAGE,
    domain=I18N_DOMAIN
)
