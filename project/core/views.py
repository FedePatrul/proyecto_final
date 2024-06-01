from django.shortcuts import render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.
def index(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "core/index.html", {"mensaje":f"Usuario '{username}' creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})

def quienes_somos(request):
    return render(request,"core/quienes_somos.html")