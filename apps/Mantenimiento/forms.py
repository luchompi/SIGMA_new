from django import forms

ESTADO = [

('activo',"En Proceso"),
('irreparable' , "Irreparable"),
('OK' , "OK"),


]

class mantenimientoForm(forms.Form):
    descripcion=forms.CharField(widget=forms.Textarea)
    observaciones=forms.CharField(widget=forms.Textarea)