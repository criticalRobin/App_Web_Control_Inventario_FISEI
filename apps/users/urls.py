from django.urls import path, include
from apps.users.views import dashboard_view  # new


app_name = 'users'  

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
]