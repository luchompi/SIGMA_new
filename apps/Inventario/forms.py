from django import forms
from apps.Personas.models import Proveedor
from .models import Marca,Modelo
class marcaForm(forms.Form):
    marca = forms.CharField()

class modeloForm(forms.Form):
    modelo = forms.CharField()

INGRESO=[
    ('donacion' , "Donacion"),
    ('compra' , "Compra directa"),
    ('comodato' , "Comodato"),
    ('transferencia' , "Transferencia tecnológica"),
    ('traspaso' , "Traspaso de otra Sede"),
]

ESTADO=[
        ('activo',"Activo"),
        ('pendiente' , "Por Asignar"),
        ('mantenimiento' , "En mantenimiento"),
        ('baja' , "En Proceso de Baja"),
]

class elementoForm(forms.Form):
    Serial=forms.CharField()
    conexionRed=forms.BooleanField()
    ip=forms.CharField()
    nombreRed=forms.CharField()
    mac=forms.CharField()
    valorAdquisicion=forms.DecimalField()
    valorActual=forms.DecimalField()
    proveedor=forms.ModelChoiceField(queryset = Proveedor.objects.all())
    marca=forms.ModelChoiceField(queryset = Marca.objects.all())
    modelo=forms.ModelChoiceField(queryset = Modelo.objects.all())
    estado=forms.Select(choices=ESTADO)
    tipoIngreso=forms.Select(choices=INGRESO)
