from django.urls import path
from . import views

app_name = "maquinas"

urlpatterns = [
    path("", views.index, name="index"),
    path("lista/", views.MaquinaList.as_view(), name="list"),
    path("crear/", views.MaquinaCreate.as_view(), name="create"),
    path("detalle/<int:pk>/", views.MaquinaDetail.as_view(), name="detail"),
    path("editar/<int:pk>/", views.MaquinaUpdate.as_view(), name="update"),
    path("eliminar/<int:pk>/", views.MaquinaDelete.as_view(), name="delete"),
]
