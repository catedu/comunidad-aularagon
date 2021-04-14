"""
WSGI config for project_conf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get("DEBUG") is None or eval(os.environ.get("DEBUG")):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_conf.settings.dev")
elif not eval(os.environ.get("DEBUG")):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_conf.settings.production")

application = get_wsgi_application()
