"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from .settings import MAIN_APP_NAME


os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{MAIN_APP_NAME}.settings')

application = get_wsgi_application()
