"""
URL configuration for inventario_FISEI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # new
from home.admin import home_admin_site
from home.views import home_view


from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="/homepage")),
    path("home/", include("home.urls")),
    path("", include("admin_argon.urls")),
    path("admin/", home_admin_site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("users/", include("apps.users.urls")),
    path("homepage/", home_view, name='home'), 
    path("main/", include("apps.main.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
