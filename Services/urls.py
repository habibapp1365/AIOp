from django.urls import path
from . import views


urlpatterns = [
    path('ssh/', views.ssh, name='ssh'),
]
