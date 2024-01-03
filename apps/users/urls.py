from django.urls import path, include
from apps.users.views import dashboard_view  # new
from .views import dashboard_view, register  # Importa la vista de registro


app_name = 'users'  

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    path("register/", register, name="register"),  # Agrega la URL de registro

]