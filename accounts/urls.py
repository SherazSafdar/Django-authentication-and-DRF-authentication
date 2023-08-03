from accounts import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import login_view
    


urlpatterns = [
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('login/', views.login_view, name='login'),
    path('login_success/', views.login_success, name='login_success'),
    path('profile/', views.profile, name='profile'),
    path('profile_create/', views.profile_create, name='profile_create'),
    path('update_profile/', views.update_profile, name='update_profile'),
    #path('forget/', views.forget_password, name='forget_password'),
    # django built in provide password change, reset etc.
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


