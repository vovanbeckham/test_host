"""
ASGI config for hoster_test project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.hoster_test.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hoster_test.settings')

application = get_asgi_application()
