from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.Inventario.models import Elemento
from django.views.generic import View
from .sessions import Baja as b

class bajaIndex(LoginRequiredMixin,View):
	login_url="/auth/login"
	def get(self,request,**kwargs):
		context={
		'query':Elemento.objects.filter(enBaja=True),
		}
		return render(request,'Bajas/index.html',context)

class add(LoginRequiredMixin,View):
	login_url = '/auth/login/'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		consulta = Elemento.objects.get(placa=ide)
		session = b(self.request)
		session.add(consulta)
		context={
		'query':Elemento.objects.filter(enBaja=True),
		}
		return render(request,'Bajas/index.html',context)

class remove(LoginRequiredMixin,View):
	login_url='/auth/login'
	def get(self,request,**kwargs):
		ide = self.kwargs['pk']
		consulta = Elemento.objects.get(placa=ide)
		session = b(self.request)
		session.remove(consulta)
		context={
		'query':Elemento.objects.filter(enBaja=True),
		}
		return render(request,'Bajas/index.html',context)

class baja(LoginRequiredMixin,View):
	login_url='/auth/login'
	def get(self,request,*args,**kwargs):
		baja = request.session["baja"]
		for row in baja.keys():
			Elemento.objects.filter(placa=baja[row]["baja_id"]).delete()
		session = b(self.request)
		session.clear()
		return redirect('bajas:bajaIndex')

class cls(LoginRequiredMixin,View):
	login_url='/auth/login'
	def get(self,request,*args,**kwargs):
		session = b(self.request)
		session.clear()
		return redirect('bajas:bajaIndex')