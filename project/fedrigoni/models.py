from django.db import models

# Create your models here.

class PDF(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.nombre
