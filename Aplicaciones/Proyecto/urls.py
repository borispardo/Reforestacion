from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaProyecto, name='lista_proyecto'),
    path('nuevo/', views.nuevoProyecto, name='nuevo_proyecto'),
    path('guardar/', views.guardarProyecto, name='guardar_proyecto'),
    path('editar/<int:id>/', views.editarProyecto, name='editar_proyecto'),
    path('procesar/', views.procesarEdicionProyecto, name='procesar_edicion_proyecto'),
    path('eliminar/<int:id>/', views.eliminarProyecto, name='eliminar_proyecto'),
]