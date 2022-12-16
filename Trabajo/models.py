from django.db import models
from datetime import date

# Create your models here.
class Trabajo(models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    descripcion = models.CharField(max_length=50)
    fecha_desde = models.DateField(default=date.today(),null=False)
    fecha_hasta = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nombre




