from django.shortcuts import render
from apps.Gestion.models import Mantenimiento,Asignacion
from apps.Inventario.models import Elemento
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import View,CreateView,UpdateView
from .forms import mantenimientoForm
class MantenimientoIndex(LoginRequiredMixin,View):
	login_url = '/auth/login/'
	def get(self,request,**kwargs):
		context={
		'query':Elemento.objects.all()
		}
		return render(request,'Mantenimiento/index.html',context)

class DetallesMantenimiento(LoginRequiredMixin,View):
	def get(self,request,**kwargs):
		obj = self.kwargs['pk']
		context = {
		'query':Asignacion.objects.get(elemento_id=obj),
		'form':mantenimientoForm,
		}
		return render(request,'Mantenimiento/detalles.html',context)