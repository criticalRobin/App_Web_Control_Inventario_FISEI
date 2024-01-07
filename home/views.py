from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth
from apps.users.models import User
from apps.main.models import Laboratory, Computer, Recommendation, Task, LabItem, ComputerItem
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView,PasswordChangeView
from .forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
# Create your views here.
def dashboard_stats_view(request):
    # Aquí puedes agregar la lógica para calcular las estadísticas de tus modelos.
    # Por ejemplo, puedes contar cuántos de cada objeto hay:
    computer_count = Computer.objects.count()
    
    # ...haz esto para cada modelo que necesites...

    # Si necesitas estadísticas mensuales como en el ejemplo, necesitarás un modelo con una fecha
    # para poder hacer un TruncMonth como se hizo con Order en tu ejemplo.
    # Vamos a asumir que tienes un modelo con una fecha y repetir el patrón:
    # items_by_month = (
    #     ModeloConFecha.objects.annotate(month=TruncMonth("fecha"))
    #     .values("month")
    #     .annotate(total=Count("id"))
    #     .order_by("month")
    # )
    # months = [item["month"].strftime("%b") for item in items_by_month]
    # totals = [item["total"] for item in items_by_month]

    # Aquí asumimos que tienes un contexto que incluye usuarios y tareas como en el ejemplo:
    users_count = User.objects.count()
    tasks_count = Task.objects.count()
     # Obtener el usuario actual, asumiendo que la solicitud está autenticada
    current_user = request.user

    # Contar las computadoras asignadas al usuario
    computers_assigned_count = Computer.objects.filter(responsible_user_id=current_user).count()

    # Contar las tareas asignadas al usuario
    tasks_assigned_count = Task.objects.filter(user_id=current_user).count()
    #contar las recomendaciones hechas por el usuario
    recommendations_count = Recommendation.objects.filter(user_id=current_user).count()
    #contar los laboratorios asignados al usuario
    laboratory_assigned_count = Laboratory.objects.filter(responsible_user_id=current_user).count()
    # Construye el contexto con la información que hayas reunido:
    
    
    #--------------------------
    computer_list = Computer.objects.filter(responsible_user_id=current_user)
    task_list = Task.objects.filter(user_id=current_user)
    recommendation_list = Recommendation.objects.filter(user_id=current_user)
    laboratory_list = Laboratory.objects.filter(responsible_user_id=current_user)
    
    context = {
        "lab_count": laboratory_assigned_count,
        "computer_count": computer_count,
      
        # ...continúa agregando el resto de las cuentas que calculaste...
        "users_count": users_count,
        "tasks_count": tasks_count,
        # "items_chart_data": {
        #     "months": months,
        #     "totals": totals,
        # },
        
        'computers_assigned_count': computers_assigned_count,
        'tasks_assigned_count': tasks_assigned_count,
        'recommendations_count': recommendations_count,
        
        #------------------
        'computer_list': computer_list,
        'task_list': task_list,
        'recommendation_list': recommendation_list,
        'laboratory_list': laboratory_list,
    }

    # No renderizamos la plantilla aquí, solo devolvemos el contexto
    return context

def argon_dashboard_view(request):
    context = dashboard_stats_view(request)
    return render(request, 'pages/dashboard.html', context)

def index(request):
  return render(request, 'pages/dashboard.html')

def billing(request):
  return render(request, 'pages/billing.html')

def profile(request):
  return render(request, 'pages/profile.html')

def tables(request):
  return render(request, 'pages/tables.html')

def rtl(request):
  return render(request, 'pages/rtl.html')

def vr(request):
  return render(request, 'pages/virtual-reality.html')

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/sign-up.html', context)


class UserLoginView(LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = LoginForm


class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')