from django import forms
from . import models

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = models.Maquina
        fields = ["nombre", "titulo", "descripcion", "pdf"]