from django.shortcuts import render
from apps.Gestion.models import Mantenimiento
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import View,CreateView,UpdateView

