from django.db import models
from Aplicaciones.Comunidad.models import Comunidad
from Aplicaciones.Especie.models import Especie

class Proyecto(models.Model):
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    archivo = models.FileField(upload_to='proyectos/', blank=True)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nombre

