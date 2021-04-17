from django.urls import path
from django.contrib.auth import views


path('', views.LoginView.as_view(template_name='login.html'), name='login')
