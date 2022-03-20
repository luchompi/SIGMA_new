from django.urls import path
from . import views as v
app_name="personas"
urlpatterns=[

#urls Funcionarios
path('funcionarios/',v.FuncionarioCreateView.as_view(),name="funcionarioIndex"),
path('funcionarios/actualizar/<pk>',v.FuncionarioUpdateView.as_view(),name="funcionarioUpdate"),
path('funcionarios/eliminar/<pk>',v.FuncionarioDelete.as_view(),name="funcionarioDelete"),

#urls Proveedores
path('proveedores/',v.ProveedorCreateView.as_view(),name="proveedorIndex"),
path('proveedores/actualizar/<pk>',v.ProveedorUpdateView.as_view(),name="proveedorUpdate"),
path('proveedores/eliminar/<pk>',v.ProveedorDelete.as_view(),name="proveedorDelete"),
]
