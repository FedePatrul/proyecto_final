from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path("contacto/", views.ClientesCreate.as_view(), name="form")
]