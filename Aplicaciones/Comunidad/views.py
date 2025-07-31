from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comunidad

#Mostrar lista de comunidades
def listaComunidad(request):
    comunidades = Comunidad.objects.all()
    return render(request, 'comunidad/lista.html', {'comunidades': comunidades})

#Mostrar formulario para crear una nueva comunidad
def nuevoComunidad(request):
    return render(request, 'comunidad/nuevo.html')

#Guardar nueva comunidad
def guardarComunidad(request):
    nombre = request.POST["nombre"]
    latitud = request.POST["latitud"]
    longitud = request.POST["longitud"]
    descripcion = request.POST["descripcion"]

    Comunidad.objects.create(
        nombre=nombre,
        latitud=latitud,
        longitud=longitud,
        descripcion=descripcion
    )

    messages.success(request, "Comunidad CREADA exitosamente")
    return redirect('/comunidad/')

#Eliminar comunidad
def eliminarComunidad(request, id):
    comunidad = Comunidad.objects.get(id=id)
    comunidad.delete()
    messages.success(request, "Comunidad ELIMINADA exitosamente")
    return redirect('/comunidad/')

#Mostrar formulario para editar comunidad
def editarComunidad(request, id):
    comunidadEditar = Comunidad.objects.get(id=id)
    return render(request, 'comunidad/editar.html', {'comunidadEditar': comunidadEditar})

#Procesar edición comunidad
def procesarEdicionComunidad(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    latitud = request.POST["latitud"]
    longitud = request.POST["longitud"]
    descripcion = request.POST["descripcion"]

    comunidad = Comunidad.objects.get(id=id)
    comunidad.nombre = nombre
    comunidad.latitud = latitud
    comunidad.longitud = longitud
    comunidad.descripcion = descripcion
    comunidad.save()

    messages.success(request, "Comunidad EDITADA exitosamente")
    return redirect('/comunidad/')
