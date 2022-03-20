from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,View
from .models import Funcionario,Proveedor
from .forms import funcionarioForm,proveedorForm

# Create your views here.
class FuncionarioCreateView(CreateView):
    model = Funcionario
    form = funcionarioForm
    fields = [    'identificacion',
    'nombres' ,
        'apellidos',
        'direccion',
        'telefono',
        'correo',
        'sede',]
    success_url='.'
    template_name='Personas/Funcionarios/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Funcionario.objects.all()
        return context
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form = funcionarioForm
    fields = ['nombres' ,
        'apellidos',
        'direccion',
        'telefono',
        'correo',
        'sede',]
    success_url="/personas/funcionarios/actualizar/{identificacion}"
    template_name='Personas/Funcionarios/update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Funcionario.objects.get(identificacion=self.kwargs['pk'])
        return context
class FuncionarioDelete(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs['pk']
        Funcionario.objects.get(identificacion=id).delete()
        return redirect('personas:funcionarioIndex')

class ProveedorCreateView(CreateView):
    model = Proveedor
    form = proveedorForm
    fields=[
        'NIT',
        'razonSocial',
        'direccion',
        'dir_venta',
        'telefono1',
        'telefono2',
        'correo',
        'vendedor',
        'tel_vendedor',
    ]
    template_name='Personas/Proveedores/index.html'
    success_url="."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = Proveedor.objects.all()
        return context
class ProveedorUpdateView(UpdateView):
        model = Proveedor
        form = proveedorForm
        fields=[
            'razonSocial',
            'direccion',
            'dir_venta',
            'telefono1',
            'telefono2',
            'correo',
            'vendedor',
            'tel_vendedor',
        ]
        template_name='Personas/Proveedores/update.html'
        success_url="/personas/proveedores/actualizar/{NIT}"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["query"] = Proveedor.objects.get(NIT=self.kwargs['pk'])
            return context
class ProveedorDelete(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs['pk']
        Proveedor.objects.get(NIT=id).delete()
        return redirect('personas:proveedorIndex')
