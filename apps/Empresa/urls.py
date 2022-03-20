from nturl2path import url2pathname
from django.urls import path
from . import views as v

app_name="empresa"

urlpatterns = [
    #Sedes Url
    path('dependencias/', v.DependenciaCreateView.as_view(), name='dependenciaIndex'),
    path('dependencias/detalles/<pk>', v.DependenciaUpdateView.as_view(), name='dependenciaUpdate'),
    path('dependencias/borrar/<pk>', v.DependenciaDelete.as_view(), name='dependenciaDelete'),

    #Dependencias Url
    path('sedes/',v.SedeCreateView.as_view(), name='sedeIndex'),
    path('sedes/borrar/<pk>', v.SedeDelete.as_view(), name='sedeDelete'),
    path('sedes/detalles/<pk>',v.SedeUpdateView.as_view(), name='sedeUpdate'),
    path('sedes/addDependencia/<pk>',v.sedeDependenciaView.as_view(),name='sedeDependencia'),
    path('sedes/addDependencia/add/<pk>',v.add.as_view(),name='add'),
    path('sedes/addDependencia/delete/<pk>',v.remove.as_view(),name='del'),
    path('sedes/addDependencia/guardar/',v.store.as_view(),name='store'),
    path('sedes/addDependencia/limpiar/',v.clear.as_view(),name='clear'),
    path('sedes/addDependencia/nuevo/<pk>',v.agregarDependencia.as_view(),name="addDependencia"),


    ]
