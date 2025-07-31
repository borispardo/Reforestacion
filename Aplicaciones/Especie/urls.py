from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaEspecie, name='lista_especie'),
    path('nuevo/', views.nuevoEspecie, name='nuevo_especie'),
    path('guardar/', views.guardarEspecie, name='guardar_especie'),
    path('editar/<int:id>/', views.editarEspecie, name='editar_especie'),
    path('procesar/', views.procesarEdicionEspecie, name='procesar_edicion_especie'),
    path('eliminar/<int:id>/', views.eliminarEspecie, name='eliminar_especie'),
]
