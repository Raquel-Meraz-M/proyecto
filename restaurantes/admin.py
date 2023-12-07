from django.contrib import admin
from restaurantes.models import Entrada,Comentario

# Registra los campos 'Entrada' y 'Comentario' de administrativa 
admin.site.register(Entrada)
admin.site.register(Comentario)
