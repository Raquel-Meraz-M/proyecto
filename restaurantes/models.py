from django.db import models

# Create your models here.
# makemigrations
# migrate 



class Entrada(models.Model):
    # Campos para almacenar el contenido de la entrada
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=800)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)

#para que devuelva una respuesta
    def __str__(self):
        return self.nombre

# Definición del modelo Comentario que representa un comentario en una entrada del blog.
class Comentario(models.Model):
    #campos para lamacenar el autor y el comentario
    nombre = models.CharField(max_length=60)
    Comentario = models.TextField(max_length=400)
    # Método que devuelve una representación legible, en este caso devuelve el nombre.
    def __str__(self):
        return self.nombre