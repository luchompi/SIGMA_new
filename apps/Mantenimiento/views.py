from django.shortcuts import redirect, render
from apps.Gestion.models import Mantenimiento,Asignacion
from apps.Inventario.models import Elemento
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import View,CreateView,UpdateView
from .forms import MantenimientoForm2, mantenimientoForm
from datetime import datetime as dt
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
		'query':Elemento.objects.get(placa=obj),
		'form':mantenimientoForm,
		}
		return render(request,'Mantenimiento/detalles.html',context)
	def post(self,request,**kwargs):
		obj = self.kwargs['pk']
		form = mantenimientoForm(request.POST)
		if form.is_valid():
			desc = form.cleaned_data['descripcion']
			query = Elemento.objects.get(placa=obj)
			query.enMantenimiento = True
			query.save()
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
		return render(request,'Mantenimiento/historial.html',context)

class DatosMantenimiento(LoginRequiredMixin,View):
	def get(self,request,**kwargs):
		obj = self.kwargs['pk']
		context={
		'query': Mantenimiento.objects.get(id=obj),
		'form': MantenimientoForm2,
		}
		return render(request,'Mantenimiento/consulta.html',context)

	def post(self,request,**kwargs):
		obj = self.kwargs['pk']
		form = MantenimientoForm2(request.POST)
		if form.is_valid():
			obs = form.cleaned_data['observaciones']
			irr= form.cleaned_data['irreparable']
			query = Mantenimiento.objects.get(id=obj)
			query.observaciones=obs
			query.finalizado=True
			query.timestampsF = dt.now()
			query.enProceso=False
			if irr:
				row = Elemento.objects.get(placa=query.elemento_id)
				row.enBaja=True
				row.esAsignado=False
				row.estado='En Proceso de Baja'
				row.enMantenimiento=False
				row.save()
				query.irreparable=irr
			else:
				row = Elemento.objects.get(placa=query.elemento_id)
				row.enMantenimiento=False
				row.save()
				query.irreparable=False
			query.save()
		return redirect('/mantenimientos/')

class ConsultaMantenimiento(LoginRequiredMixin,View):
	login_url='/auth/login'
	def get(self,request,**kwargs):
		q = self.kwargs['pk']
		context={
		'query':Mantenimiento.objects.get(id=q),
		}
		return render(request,'Mantenimiento/datos.html',context)