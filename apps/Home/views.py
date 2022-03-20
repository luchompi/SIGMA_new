from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class index(LoginRequiredMixin,TemplateView):
	login_url="/auth/login"
	template_name = "Home/index.html"