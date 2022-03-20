from django.urls import path
from . import views as v

app_name="gestion"

urlpatterns=[
#Asignaciones
path('',v.Asignar.as_view(),name="asignacionIndex"),
path('add2SessionF/<pk>',v.add2SessionF.as_view(),name="add2SessionF"),
path('del2SessionF/',v.del2SessionF.as_view(),name="del2SessionF"),
path('add2Asig/<pk>',v.add2Asig.as_view(),name="add2Asig"),
path('del2Asig/<pk>',v.del2Asig.as_view(),name="del2Asig"),
path('cancelar/',v.cancel.as_view(),name="cancel"),
path('procesar/',v.Asig2func.as_view(),name="procesar"),
path('consultar/',v.query.as_view(),name="consulta"),
path('query/<pk>',v.funcQuery.as_view(),name="query"),
]