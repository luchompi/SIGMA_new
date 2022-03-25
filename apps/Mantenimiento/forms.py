from django import forms


class mantenimientoForm(forms.Form):
    descripcion=forms.CharField(widget=forms.Textarea)


class MantenimientoForm2(forms.Form):
    observaciones=forms.CharField(widget=forms.Textarea)
    