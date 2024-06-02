from django import forms
from . import models

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido", "email", "fecha_de_nacimiento", "mensaje"]