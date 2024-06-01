from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("quienes-somos", views.quienes_somos, name="quienes_somos"),
]
