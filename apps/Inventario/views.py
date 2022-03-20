from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,View
from .models import Marca,Modelo,Elemento
from .forms import marcaForm,modeloForm,elementoForm
# Procedimientos con Marcas
class MarcaCreate(CreateView):
    model = Marca
    fields = ['marca',]
    form = marcaForm
    success_url='.'
    template_name="Inventario/Marcas/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Marca.objects.all()
        return context


class MarcaUpdate(UpdateView):
    model = Marca
    fields = ['marca',]
    form = marcaForm
    success_url="/inventario/marcas/detalles/{id}"
    template_name="Inventario/Marcas/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Marca.objects.get(id=self.kwargs['pk'])
        return context


class MarcaDelete(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs['pk']
        Marca.objects.get(id=id).delete()
        return redirect('inventario:marcaIndex')


#Procedimientos con Modelos
class ModeloCreate(CreateView):
    model = Modelo
    fields = ['modelo',]
    form = modeloForm
    success_url='.'
    template_name="Inventario/Modelos/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Modelo.objects.all()
        return context

class ModeloUpdate(UpdateView):
        model = Modelo
        fields = ['modelo',]
        form = modeloForm
        success_url="/inventario/modelos/detalles/{id}"
        template_name="Inventario/Modelos/update.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["query"] = Modelo.objects.get(id=self.kwargs['pk'])
            return context

class ModeloDelete(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs['pk']
        Modelo.objects.get(id=id).delete()
        return redirect('inventario:modeloIndex')

#Procedimientos de Elementos
class ElementoCreate(CreateView):
    model = Elemento
    fields=[
    'Serial',
    'conexionRed',
    'ip',
    'nombreRed',
    'mac',
    'valorAdquisicion',
    'valorActual',
    'proveedor',
    'marca',
    'modelo',
    'estado',
    'tipoIngreso',
    ]
    form = elementoForm
    success_url ='.'
    template_name="Inventario/Elementos/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Elemento.objects.all()
        return context

class ElementoUpdate(UpdateView):
    model = Elemento
    fields=[
    'Serial',
    'conexionRed',
    'ip',
    'nombreRed',
    'mac',
    'valorAdquisicion',
    'valorActual',
    'proveedor',
    'marca',
    'modelo',
    'estado',
    'tipoIngreso',
    ]
    form = elementoForm
    success_url ="/inventario/elementos/detalles/{placa}"
    template_name="Inventario/Elementos/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Elemento.objects.get(placa=self.kwargs['pk'])
        return context



class ElementoDelete(View):
    def get(self,request,*args,**kwargs):
        id =self.kwargs['pk']
        Elemento.objects.get(placa=id).delete()
        return redirect('inventario:elementoIndex')
