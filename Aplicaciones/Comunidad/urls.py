from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaComunidad, name='lista_comunidad'),
    path('nuevo/', views.nuevoComunidad, name='nuevo_comunidad'),
    path('guardar/', views.guardarComunidad, name='guardar_comunidad'),
    path('editar/<int:id>/', views.editarComunidad, name='editar_comunidad'),
    path('procesar/', views.procesarEdicionComunidad, name='procesar_edicion_comunidad'),
    path('eliminar/<int:id>/', views.eliminarComunidad, name='eliminar_comunidad'),
    path('enviar/<int:id>/', views.enviarMensajeComunidad, name='enviar_mensaje'),
    path('dashboard/', views.dashboard, name='dashboard'),
]