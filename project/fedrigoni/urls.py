from django.urls import path
from . import views

app_name = "fedrigoni"

urlpatterns = [
    path("", views.index, name="index"),
    path('fichas-tecnicas/', views.list_pdfs, name='list_pdfs'),
    path('download/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
]