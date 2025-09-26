from django.apps import AppConfig

from ..settings import MAIN_APP_NAME


class CasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'{MAIN_APP_NAME}.cases'
