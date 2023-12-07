"""
ASGI config for proyecto1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#Establece el módulo de configuración predeterminado de Django para el proyecto 'proyecto1'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto1.settings')

# Obtiene la aplicación ASGI para el proyecto 'proyecto1'.
application = get_asgi_application()
