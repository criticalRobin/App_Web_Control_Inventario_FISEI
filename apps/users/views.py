from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,  authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreationForm


@login_required
def dashboard_view(request):
    # Tu lógica aquí
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})