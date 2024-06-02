from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    mensaje = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
