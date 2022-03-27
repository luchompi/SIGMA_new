from django.urls import path
from . import views as v

app_name="mantenimiento"

urlpatterns=[
path('',v.MantenimientoIndex.as_view(),name="mantIndex"),
path('detalles/<pk>',v.DetallesMantenimiento.as_view(),name="mantDetail"),
path('historial/<pk>',v.HistorialMantenimiento.as_view(),name="mantHistorial"),
path('query/<pk>',v.DatosMantenimiento.as_view(),name="mantQuery"),
path('request/<pk>',v.ConsultaMantenimiento.as_view(),name="mantData"),
]