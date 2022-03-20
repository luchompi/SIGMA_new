from django import forms
from apps.Empresa.models import SedeDependencia
class funcionarioForm(forms.Form):
        identificacion= forms.IntegerField()
        nombres = forms.CharField()
        apellidos = forms.CharField()
        direccion = forms.CharField()
        telefono = forms.CharField()
        correo = forms.EmailField()
        sede = forms.ModelChoiceField(queryset=SedeDependencia.objects.all())


class proveedorForm(forms.Form):
    NIT=forms.CharField()
    razonSocial=forms.CharField()
    direccion=forms.CharField()
    dir_venta=forms.CharField()
    telefono1=forms.CharField()
    telefono2=forms.CharField()
    correo=forms.EmailField()
    vendedor=forms.CharField()
    tel_vendedor=forms.CharField()
