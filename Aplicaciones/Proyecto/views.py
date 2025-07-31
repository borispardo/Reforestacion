from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Proyecto
from Aplicaciones.Comunidad.models import Comunidad
from Aplicaciones.Especie.models import Especie

#Mostrar lista de proyectos
def listaProyecto(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto/lista.html', {'proyectos': proyectos})

#Mostrar formulario para crear un nuevo proyecto
def nuevoProyecto(request):
    comunidades = Comunidad.objects.all()
    especies = Especie.objects.all()
    return render(request, 'proyecto/nuevo.html', {
        'comunidades': comunidades, 
        'especies': especies
    })

#Guardar nuevo proyecto
def guardarProyecto(request):
    comunidad_id = request.POST["comunidad"]
    especie_id = request.POST["especie"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    archivo = request.FILES.get("archivo", None)

    Proyecto.objects.create(
        comunidad_id=comunidad_id,
        especie_id=especie_id,
        nombre=nombre,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        archivo=archivo
    )
    messages.success(request, "Proyecto CREADO exitosamente")
    return redirect('/proyecto/')

#Eliminar proyecto
def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    messages.success(request, "Proyecto ELIMINADO exitosamente")
    return redirect('/proyecto/')

#Mostrar formulario para editar proyecto
def editarProyecto(request, id):
    proyectoEditar = Proyecto.objects.get(id=id)
    comunidades = Comunidad.objects.all()
    especies = Especie.objects.all()
    return render(request, 'proyecto/editar.html', {
        'proyectoEditar': proyectoEditar,
        'comunidades': comunidades,
        'especies': especies
    })

#Procesar edición proyecto
def procesarEdicionProyecto(request):
    id = request.POST["id"]
    comunidad_id = request.POST["comunidad"]
    especie_id = request.POST["especie"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    archivo = request.FILES.get("archivo", None)

    proyecto = Proyecto.objects.get(id=id)
    proyecto.comunidad_id = comunidad_id
    proyecto.especie_id = especie_id
    proyecto.nombre = nombre
    proyecto.descripcion = descripcion
    proyecto.fecha_inicio = fecha_inicio
    proyecto.fecha_fin = fecha_fin
    proyecto.archivo = archivo
    proyecto.save()

    messages.success(request, "Proyecto EDITADO exitosamente")
    return redirect('/proyecto/')
