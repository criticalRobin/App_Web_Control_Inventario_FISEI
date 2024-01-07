from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path
from .views import dashboard_stats_view

# from apps.views import dashboard_stats_view
from apps.main.models import *
from apps.users.models import User

# Register your models here.

class HomeAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        context = dashboard_stats_view(request)
        if isinstance(extra_context, dict):
            extra_context.update(context)
        return super().index(request, extra_context)

home_admin_site = HomeAdminSite(name="home_admin")

home_admin_site.register(User)
home_admin_site.register(Laboratory)
home_admin_site.register(Computer)
home_admin_site.register(Recommendation)
home_admin_site.register(Task)
home_admin_site.register(LabItem)
home_admin_site.register(ComputerItem)
