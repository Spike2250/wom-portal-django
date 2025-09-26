from django.apps import AppConfig

from ..settings import MAIN_APP_NAME


class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'{MAIN_APP_NAME}.patients'
