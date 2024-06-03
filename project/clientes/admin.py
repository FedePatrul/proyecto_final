from django.contrib import admin
from .models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display= (
        "nombre",
        "apellido",
        "email",
        "telefono",
        "fecha_de_nacimiento",
        "mensaje",
    )
    list_display_links = ("nombre", )

admin.site.register(Cliente, ClienteAdmin)