from django.db import models

from apps.Personas.models import Proveedor

class Marca(models.Model):
    marca = models.CharField(max_length=50,unique=True, error_messages={'unique':'Esta Marca ya se encuentra Registrada'})
    timestamps=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return '%s'%(self.marca)

class Modelo(models.Model):
    modelo = models.CharField(max_length=150,unique=True,error_messages={'unique':'Ya está registrado este modelo'})
    timestamps=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s'%(self.modelo)

class Elemento(models.Model):
    class Estado(models.TextChoices):
        activo='Activo'
        pendiente = 'Por Asignar'
        mantenimiento = 'En mantenimiento'
        baja = 'En Proceso de Baja'

    class Ingresos(models.TextChoices):
        donacion = 'Donacion'
        compra = 'Compra directa'
        comodato = 'Comodato'
        transferencia = 'Transferencia tecnológica'
        traspaso = 'Traspaso de otra Sede'
    placa=models.AutoField(primary_key=True)
    Serial=models.CharField(max_length=100,verbose_name="Serial del Elemento",unique=True,error_messages={'unique':'Ya existe un elemento con este Serial'})
    conexionRed=models.BooleanField(default=False,verbose_name="Está conectado a la red?")
    ip=models.CharField(max_length=100,null=True,blank=True,verbose_name="Dirección IP",unique=True,error_messages={'unique':'Ya existe un elemento con esta IP'})
    nombreRed=models.CharField(max_length=100,verbose_name="Nombre en la red",null=True,blank=True)
    mac=models.CharField(max_length=100,verbose_name="Dirección MAC",null=True,blank=True,unique=True,error_messages={'unique':'Ya existe un elemento con este MAC'})
    valorAdquisicion=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor de adquisición")
    valorActual=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor actual")
    fechaAdquisicion=models.DateField(verbose_name="Fecha de adquisición",auto_now=True)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Proveedor")
    marca=models.ForeignKey(Marca,on_delete=models.CASCADE,verbose_name="Marca del Elemento")
    modelo=models.ForeignKey(Modelo,on_delete=models.CASCADE,verbose_name="Modelo del Elemento")
    estado=models.CharField(choices=Estado.choices,default='Activo', max_length=50)
    tipoIngreso=models.CharField(choices=Ingresos.choices,default='Compra directa',max_length=150)
    esAsignado=models.BooleanField(default=False)
    enMantenimiento=models.BooleanField(default=False)
    enBaja=models.BooleanField(default=False)
    timestamps=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ="Elemento"
        verbose_name_plural ="Elementos"

    def __str__(self):
        return '%s %s %s'%(self.placa,self.marca,self.modelo)
