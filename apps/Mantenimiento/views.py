from django.shortcuts import redirect, render
from apps.Gestion.models import Mantenimiento,Asignacion
from apps.Inventario.models import Elemento
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import View,CreateView,UpdateView
from .forms import MantenimientoForm2, mantenimientoForm
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
	def post(self,request,**kwargs):
		obj = self.kwargs['pk']
		form = mantenimientoForm(request.POST)
		if form.is_valid():
			desc = form.cleaned_data['descripcion']
			
			Mantenimiento.objects.create(descripcion=desc,user=self.request.user.username,elemento_id=obj,enProceso=True)
			return redirect('/mantenimientos/')

class HistorialMantenimiento(LoginRequiredMixin,View):
	login_url='/auth/login/'
	def get(self,request,**kwargs):
		obj = self.kwargs['pk']
		context = {
		'query':Mantenimiento.objects.filter(elemento_id=obj),
		'consulta': Elemento.objects.get(placa=obj),
		}
		print(Mantenimiento.objects.filter(elemento_id=obj))

		return render(request,'Mantenimiento/historial.html',context)

class DatosMantenimiento(LoginRequiredMixin,View):
	def get(self,request,**kwargs):
		obj = self.kwargs['pk']
		context={
		'query': Mantenimiento.objects.get(id=obj),
		'form': MantenimientoForm2,
		}
		return render(request,'Mantenimiento/consulta.html',context)


