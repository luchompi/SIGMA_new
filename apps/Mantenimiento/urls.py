from django.urls import path
from . import views as v

app_name="mantenimiento"

urlpatterns=[
path('',v.MantenimientoIndex.as_view(),name="mantIndex"),
path('detalles/<pk>',v.DetallesMantenimiento.as_view(),name="mantDetail"),

]