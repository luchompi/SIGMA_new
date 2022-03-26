from django.urls import path 
from . import views as v

app_name="bajas"

urlpatterns=[
path('',v.bajaIndex.as_view(),name="bajaIndex"),
path('add/<pk>',v.add.as_view(),name="bajaAdd"),
path('remove/<pk>',v.remove.as_view(),name="bajaRemove"),
path('authorize/',v.baja.as_view(),name="baja"),
path('cls/',v.cls.as_view(),name="cls"),
]