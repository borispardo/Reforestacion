from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comunidad
from django.core.mail import EmailMessage
from django.conf import settings
import mimetypes

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

#Enviar mensaje a comunidad
def enviarMensajeComunidad(request, id):
    comunidad = get_object_or_404(Comunidad, id=id)

    if request.method == 'POST':
        destinatario = request.POST.get('destinatario')
        asunto = request.POST.get('asunto', '')
        mensaje = request.POST.get('mensaje', '')
        archivo = request.FILES.get('archivo', None)

        email = EmailMessage(
            subject=asunto,
            body=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[destinatario]
        )

        if archivo:
            tipo_mime, _ = mimetypes.guess_type(archivo.name)
            email.attach(archivo.name, archivo.read(), tipo_mime or 'application/octet-stream')

        try:
            email.send()
            messages.success(request, "Mensaje enviado exitosamente")
        except Exception as e:
            messages.error(request, f"Error al enviar el mensaje: {str(e)}")

        return redirect('/comunidad/')

    return render(request, 'comunidad/enviar.html', {
        'comunidad': comunidad})
