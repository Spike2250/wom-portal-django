"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from .settings import MAIN_APP_NAME


os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{MAIN_APP_NAME}.settings')

application = get_asgi_application()
