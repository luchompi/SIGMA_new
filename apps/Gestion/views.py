from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Asignacion,Mantenimiento
from .sessions import Asignacion as asig,Funcionario as fc
from apps.Personas.models import Funcionario
from apps.Inventario.models import Elemento

#Procedimiento de Asignaciones
class Asignar(View):
	def get(self,request,**kwargs):
		context={
		'personas' : Funcionario.objects.all(),
		'query' : Elemento.objects.filter(esAsignado=False)
		}
		return render(request,'Asignacion/index.html',context)

class add2SessionF(View):
	def get(self,request,**kwargs):
		query = Funcionario.objects.get(identificacion=self.kwargs['pk'])
		funcionario = fc(self.request)
		if query:
			funcionario.add(query)
			context={'query':Elemento.objects.filter(esAsignado=False)}
			return render(request,'Asignacion/index.html',context)

class del2SessionF(View):
	def get(self,request,**kwargs):
		funcionario = fc(self.request)
		funcionario.clear()
		context={
		'personas' : Funcionario.objects.all(),
		'query' : Elemento.objects.filter(esAsignado=False)
		}
		return render(request,'Asignacion/index.html',context)

class add2Asig(View):
	def get(self,request,**kwargs):
		obj = Elemento.objects.get(placa=self.kwargs['pk'])
		if obj:
			func = asig(self.request)
			func.add(obj)
			context={
			'personas' : Funcionario.objects.all(),
			'query' : Elemento.objects.filter(esAsignado=False)
			}
			return render(request,'Asignacion/index.html',context)

class del2Asig(View):
	def get(self,request,**kwargs):
		obj = Elemento.objects.get(placa = self.kwargs['pk'])
		if obj:
			func = asig(self.request)
			func.remove(obj)
			context={
			'personas' : Funcionario.objects.all(),
			'query' : Elemento.objects.filter(esAsignado=False)
			}
			return render(request,'Asignacion/index.html',context)

class Asig2func(View):
	def get(self,request,**kwargs):
		elemento = asig(self.request)
		func = fc(self.request)
		obj = request.session["asignacion"]
		persona = request.session["funcionario"]
		for row in persona.keys():
			aux = persona[row]["funcionario_id"]
		for row in obj.keys():
			element = obj[row]["asignacion_id"]
			Asignacion.objects.create(funcionario_id=aux,elemento_id=element,user=request.user.username)
			a = Elemento.objects.get(placa=element)
			a.esAsignado=True
			a.save()
		elemento.clear()
		func.clear()
		return render(request,'Asignacion/asignaciones.html',context={'query':Funcionario.objects.all()})

class cancel(View):
	def get(self,request,**kwargs):
		elemento = asig(self.request)
		func = fc(self.request)
		elemento.clear()
		func.clear()
		return redirect('asignacion:consulta')

#Procedimientos de consulta de asignaciones
class query(View):
	def get(self,request,**kwargs):
		return render(request,'Asignacion/asignaciones.html',context={'query':Funcionario.objects.all()})


class funcQuery(View):
	def get(self,request,**kwargs):
		context={
		'query': Asignacion.objects.filter(funcionario_id=self.kwargs['pk']),
		'func': Funcionario.objects.get(identificacion=self.kwargs['pk'])
		}
		return render(request,'Asignacion/consulta.html', context)