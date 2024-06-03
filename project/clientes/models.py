from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    telefono = models.IntegerField(unique=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True, default=timezone.now, help_text="dd/mm/aaaa")
    mensaje = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
