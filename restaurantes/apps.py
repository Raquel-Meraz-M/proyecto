from django.apps import AppConfig


class RestaurantesConfig(AppConfig):
    # para especificar el tipo de campo automático por defecto para las claves primarias
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurantes'
