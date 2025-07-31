from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Especie

def home(request):
    return render(request, 'home.html') 
    
#Mostrar lista de especies
def listaEspecie(request):
    especies = Especie.objects.all()
    return render(request, 'especie/lista.html', {'especies': especies})

#Mostrar formulario para crear una nueva especie
def nuevoEspecie(request):
    return render(request, 'especie/nuevo.html')

#Guardar nueva especie
def guardarEspecie(request):
    nombre_comun = request.POST["nombre_comun"]
    nombre_cientifico = request.POST["nombre_cientifico"]
    imagen = request.FILES.get("imagen", None)

    Especie.objects.create(
        nombre_comun=nombre_comun,
        nombre_cientifico=nombre_cientifico,
        imagen=imagen
    )

    messages.success(request, "Especie CREADA exitosamente")
    return redirect('/especie/')

#Eliminar especie
def eliminarEspecie(request, id):
    especie = Especie.objects.get(id=id)
    especie.delete()
    messages.success(request, "Especie ELIMINADA exitosamente")
    return redirect('/especie/')

#Mostrar formulario para editar especie
def editarEspecie(request, id):
    especieEditar = Especie.objects.get(id=id)
    return render(request, 'especie/editar.html', {'especieEditar': especieEditar})

#Procesar edición especie
def procesarEdicionEspecie(request):
    id = request.POST["id"]
    nombre_comun = request.POST["nombre_comun"]
    nombre_cientifico = request.POST["nombre_cientifico"]
    imagen = request.FILES.get("imagen", None)

    especie = Especie.objects.get(id=id)
    especie.nombre_comun = nombre_comun
    especie.nombre_cientifico = nombre_cientifico
    if imagen:
        especie.imagen = imagen
    especie.save()

    messages.success(request, "Especie EDITADA exitosamente")
    return redirect('/especie/')