"""
WSGI config for project_conf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

environment = (
    "dev" if os.environ.get("SETTINGS_SELECTION") in ["dev", None] else "production"
)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"project_conf.settings.{environment}"
)

application = get_wsgi_application()
