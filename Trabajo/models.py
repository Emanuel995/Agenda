from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Trabajo(models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    descripcion = models.CharField(max_length=50)
    fecha_desde = models.DateField(default=timezone.now,null=False)
    fecha_hasta = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nombre




