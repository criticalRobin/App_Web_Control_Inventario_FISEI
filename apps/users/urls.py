from django.urls import path, include
from apps import users
from apps.users.views import dashboard_view  # new

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
]