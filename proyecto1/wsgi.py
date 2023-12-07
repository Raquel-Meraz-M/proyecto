"""
WSGI config for proyecto1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
# Importación del módulo 'os' para interactuar con el sistema operativo.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto1.settings')

# Obtención de la aplicación WSGI y asignación a la variable 'application'.
application = get_wsgi_application()
