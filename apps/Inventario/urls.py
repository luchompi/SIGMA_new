from django.urls import path
from . import views as v
app_name="inventario"
urlpatterns=[

#url Marcas
path('marcas/',v.MarcaCreate.as_view(),name="marcaIndex"),
path('marcas/detalles/<pk>',v.MarcaUpdate.as_view(),name="marcaUpdate"),
path('marcas/eliminar/<pk>',v.MarcaDelete.as_view(),name="marcaDelete"),

#url Modelo
path('modelos/',v.ModeloCreate.as_view(),name="modeloIndex"),
path('modelos/detalles/<pk>',v.ModeloUpdate.as_view(),name="modeloUpdate"),
path('modelos/eliminar/<pk>',v.ModeloDelete.as_view(),name="modeloDelete"),

#url Elementos
path('elementos/',v.ElementoCreate.as_view(),name="elementoIndex"),
path('elementos/detalles/<pk>',v.ElementoUpdate.as_view(),name="elementoUpdate"),
path('elementos/eliminar/<pk>',v.ElementoDelete.as_view(),name="elementoDelete"),
]
