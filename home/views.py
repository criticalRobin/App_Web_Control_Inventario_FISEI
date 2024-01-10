from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth
from apps.users.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from apps.main.models import Recommendation
from apps.main.forms import StudentRecommendationForm
from apps.main.models import (
    Laboratory,
    Computer,
    Recommendation,
    Task,
    LabItem,
    ComputerItem,
)
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordChangeView,
)
from .forms import (
    RegistrationForm,
    LoginForm,
    UserPasswordResetForm,
    UserSetPasswordForm,
    UserPasswordChangeForm,
)
import datetime
from django.db.models.functions import ExtractMonth


# Create your views here.
def dashboard_stats_view(request):
    computer_count = Computer.objects.count()
    users_count = User.objects.count()
    tasks_count = Task.objects.count()
    current_user = request.user
    reccoms_count = Recommendation.objects.count()
    labs_count = Laboratory.objects.count()

    computers_assigned_count = Computer.objects.filter(
        responsible_user_id=current_user
    ).count()

    tasks_assigned_count = Task.objects.filter(user_id=current_user).count()
    recommendations_count = Recommendation.objects.filter(user_id=current_user).count()
    laboratory_assigned_count = Laboratory.objects.filter(
        responsible_user_id=current_user
    ).count()

    computer_list = Computer.objects.filter(responsible_user_id=current_user)
    task_list = Task.objects.filter(user_id=current_user)
    recommendation_list = Recommendation.objects.filter(user_id=current_user)
    laboratory_list = Laboratory.objects.filter(responsible_user_id=current_user)

    current_year = datetime.datetime.now().year
    tasks_created_monthly = (
        Task.objects.filter(date__year=current_year)
        .annotate(month=ExtractMonth("date"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("month")
    )

    context = {
        "tasks_created_monthly": tasks_created_monthly,
        "lab_count": laboratory_assigned_count,
        "computer_count": computer_count,
        "reccoms_count": reccoms_count,
        "labs_count": labs_count,
        "users_count": users_count,
        "tasks_count": tasks_count,
        "computers_assigned_count": computers_assigned_count,
        "tasks_assigned_count": tasks_assigned_count,
        "recommendations_count": recommendations_count,
        "computer_list": computer_list,
        "task_list": task_list,
        "recommendation_list": recommendation_list,
        "laboratory_list": laboratory_list,
    }

    return context


def argon_dashboard_view(request):
    context = dashboard_stats_view(request)
    return render(request, "pages/dashboard.html", context)


def index(request):
    return render(request, "pages/dashboard.html")


def billing(request):
    return render(request, "pages/billing.html")


def profile(request):
    return render(request, "pages/profile.html")


def tables(request):
    return render(request, "pages/tables.html")


def rtl(request):
    return render(request, "pages/rtl.html")


def vr(request):
    return render(request, "pages/virtual-reality.html")


def home_view(request):
    if request.method == "POST":
        form = StudentRecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            
            # Obtener el objeto Laboratory desde el formulario
            lab = form.cleaned_data['id_lab']

            # Asignar el ID del laboratorio a la recomendación
            recommendation.id_lab_id = lab.id

            # Establecer el usuario por defecto (ID 3)
            recommendation.user_id_id = 3
            
            recommendation.date = timezone.now()
            recommendation.save()
            
            messages.add_message(request, messages.INFO, 'Se envió la recomendación con éxito.', extra_tags='form_message')
            form = StudentRecommendationForm()

    else:
        form = StudentRecommendationForm()

    return render(request, 'home_page.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created successfully!")
            return redirect("/accounts/login/")
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "accounts/sign-up.html", context)


class UserLoginView(LoginView):
    template_name = "accounts/sign-in.html"
    form_class = LoginForm

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return "/admin/"  # O la URL que quieras para superusuarios
        return super().get_success_url()


class UserPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    form_class = UserSetPasswordForm


class UserPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change.html"
    form_class = UserPasswordChangeForm


def user_logout_view(request):
    logout(request)
    return redirect("/homepage")
