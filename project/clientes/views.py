from django.shortcuts import render
from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Cliente

# Create your views here.

class ClientesCreate(CreateView):
    model = Cliente
    form_class = forms.MaquinaForm
    success_url = reverse_lazy("core:index")