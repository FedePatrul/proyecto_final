from django.shortcuts import render
from .models import Maquina
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, "maquinas/index.html")

class MaquinaList(ListView):
    model =  Maquina

class MaquinaCreate(LoginRequiredMixin, CreateView):
    model = Maquina
    form_class = forms.MaquinaForm
    success_url = reverse_lazy("maquinas:list")

class MaquinaDetail(DetailView):
    model =  Maquina

class MaquinaUpdate(LoginRequiredMixin, UpdateView):
    model = Maquina
    form_class = forms.MaquinaForm
    success_url = reverse_lazy("maquinas:list")

class MaquinaDelete(LoginRequiredMixin, DeleteView):
    model = Maquina
    success_url = reverse_lazy("maquinas:list")

