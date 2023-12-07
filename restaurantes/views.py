# Importaciones necesarias
from django.shortcuts import render
from restaurantes.models import Entrada, Comentario

# Definición de vistas
def home(request):
    # Obtener todas las entradas de restaurantes
    Restaurantes = Entrada.objects.all()
    
    # Verificar si la solicitud es de tipo POST
    if request.method == "POST":
        # Obtener datos del formulario
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        
        # Crear un nuevo comentario y guardarlo en la base de datos
        obj = Comentario(nombre=nombre, Comentario=mensaje)
        obj.save()
        
        # Configurar un mensaje de agradecimiento
        mensaje = "Gracias por tu comentario"
        
        # Renderizar la página con la lista de restaurantes y el mensaje
        return render(request, "home.html", {"Restaurantes": Restaurantes, "mensaje": mensaje})
    
    # Renderizar la página con la lista de restaurantes
    return render(request, "home.html", {"Restaurantes": Restaurantes})

# Vista para la página "Conocenos"
def conoce(request):
    # Obtener todas las entradas de restaurantes
    Restaurantes = Entrada.objects.all()
    
    # Renderizar la página "Conocenos" sin datos adicionales
    return render(request, "Conocenos.html")

# Vista para la página "Galeria"
def galeria(request):
    # Obtener todas las entradas de restaurantes
    Restaurantes = Entrada.objects.all()
    
    # Renderizar la página "Galeria" sin datos adicionales
    return render(request, "Galeria.html")
