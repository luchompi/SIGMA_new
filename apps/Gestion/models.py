from pyexpat import model
from django.db import models
from apps.Inventario.models import Elemento
from apps.Personas.models import Funcionario

# Create your models here.
class Asignacion(models.Model):
    funcionario=models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    elemento=models.ForeignKey(Elemento,on_delete=models.CASCADE)
    user=models.CharField(max_length=50) 
    timestamps=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"

    def __str__(self):
        return '%s %s'%(self.funcionario,self.elemento)

class Mantenimiento(models.Model):
    class Estado(models.TextChoices):
        activo='En Proceso'
        irreparable = 'Irreparable'
        OK = 'OK'    
    elemento=models.ForeignKey(Elemento,on_delete=models.CASCADE)
    deBaja=models.BooleanField(default=False)
    descripcion=models.TextField(max_length=20000000000)
    fecha=models.DateTimeField(auto_now=True)
    user=models.CharField(max_length=50)
    observaciones=models.TextField(max_length=20000000000)
    enProceso=models.BooleanField(default=False)
    finalizado=models.BooleanField(default=False)
    irreparable=models.BooleanField(default=False)
    timestamps=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mantenimiento"
        verbose_name_plural = "Mantenimientos"

    def __str__(self):
        return '%s %s'%(self.elemento,self.estado)
