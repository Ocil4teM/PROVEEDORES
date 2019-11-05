from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Proveedor


# Create your views here.
class ProveedorView(LoginRequiredMixin, generic.ListView):
     model = Proveedor
     template_name = "inv/proveedor_list.html"
     context_object_name = "obj"
     login_url = "bases:login"