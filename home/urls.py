from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .views import home_view


app_name = 'home'

urlpatterns = [
    path('', argon_dashboard_view, name='index'),
    path('billing/', billing, name='billing'),
    path('profile/', profile, name='profile'),
    path('tables/',  tables,  name='tables' ),
    path('rtl/',     rtl,     name='rtl'    ),
    path('vr/',      vr,      name='vr'     ),

    # Authentication
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', user_logout_view, name='logout'),
    path('accounts/register/', register, name='register'),
    path('accounts/password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
       UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('homepage/', home_view, name='home'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
