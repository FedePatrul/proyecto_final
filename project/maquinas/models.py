from django.db import models

# Create your models here.
class Maquina(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    pdf = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "maquina"
        verbose_name_plural = "maquinas"


