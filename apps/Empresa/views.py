from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,View,UpdateView
from .insertion import sede as s, Detalle as d
from apps.Empresa.forms import DependenciaForm,SedeForm,addDependenciaForm
from .models import Dependencia,Sede,SedeDependencia
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.

#Operaciones con Dependencias
class DependenciaCreateView(LoginRequiredMixin,CreateView):
    login_url='/auth/login'
    model = Dependencia
    fields = ['dependencia',]
    template_name = 'Empresa/Dependencia/index.html'
    success_url = '.'
    form = DependenciaForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Dependencia.objects.all()
        return context

class DependenciaDelete(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        id = kwargs['pk']
        Dependencia.objects.get(id=id).delete()
        return redirect('empresa:dependenciaIndex')


class DependenciaUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/auth/login'
    model = Dependencia
    template_name = "Empresa/Dependencia/update.html"
    form = DependenciaForm
    fields = ['dependencia',]
    success_url = '.'



#Operaciones Con sedes
class SedeCreateView(LoginRequiredMixin,CreateView):
    login_url='/auth/login'
    model= Sede
    form = SedeForm
    fields = ['sede',]
    success_url = '.'
    template_name = 'Empresa/Sede/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Sede.objects.all()
        return context
    def form_valid(self,form):
        form.save()
        sede = form.cleaned_data['sede']
        queryset = Sede.objects.get(sede=sede)
        sede = s(self.request)
        sede.add(queryset)
        return redirect('empresa:sedeDependencia',queryset.id)

class sedeDependenciaView(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        pk=(self.kwargs['pk'])
        context={
        'sede':Sede.objects.get(id=pk),
        'query':Dependencia.objects.all(),
        }
        return render(request,'Empresa/Sede/detalles.html',context)

class SedeUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/auth/login'
    model = Sede
    form = SedeForm
    fields = ['sede',]
    success_url = '/empresa/sedes/detalles/{id}'
    template_name = 'Empresa/Sede/update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dep"] = SedeDependencia.objects.filter(sede=self.object)
        return context



class SedeDelete(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        id = kwargs['pk']
        Sede.objects.get(id=id).delete()
        return redirect('empresa:sedeIndex')

class add(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        query = Dependencia.objects.get(id=self.kwargs['pk'])
        if query:
            dependencia =d(self.request)
            dependencia.add(query)
            aux = request.session["sede"]
            for row in aux.keys():
                id=aux[row]['sede_id']
            return redirect('empresa:sedeDependencia',str(id))

class clear(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        dependencia =d(self.request)
        dependencia.clear()
        aux = request.session["sede"]
        for row in aux.keys():
            id=aux[row]['sede_id']
        return redirect('empresa:sedeDependencia',str(id))

class remove(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        query = Dependencia.objects.get(id=kwargs['pk'])
        dep = d(self.request)
        dep.remove(query)
        aux = request.session["sede"]
        for row in aux.keys():
            id=aux[row]['sede_id']
        return redirect('empresa:sedeDependencia',str(id))

class store(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        sede = request.session["sede"]
        dep = request.session["detalle"]
        for row in sede.keys():
            s = sede[row]["sede_id"]
        for row in dep.keys():
            d = dep[row]["dependencia_id"]
            SedeDependencia.objects.create(sede_id=s,dependencia_id=d)
        sede.clear()
        dep.clear()
        return redirect('empresa:sedeUpdate',str(s))

class agregarDependencia(LoginRequiredMixin,View):
    login_url='/auth/login'
    def get(self,request,*args,**kwargs):
        context={
        'form':addDependenciaForm,
        'query':SedeDependencia.objects.filter(sede_id=self.kwargs['pk']),
        'object':Sede.objects.get(id=self.kwargs['pk']),
        }
        return render (request,'Empresa/Sede/addDependencia.html',context)
    def post(self,request,*args,**kwargs):
        form = addDependenciaForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['dependencia']
            SedeDependencia.objects.create(sede_id=self.kwargs['pk'],dependencia=query)
            return redirect('empresa:sedeUpdate',self.kwargs['pk'])
