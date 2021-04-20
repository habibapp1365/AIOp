from django.urls import path
from . import views


urlpatterns = [

    path('', views.div, name='div'),
    path('d', views.dashboard, name='dashboard'),
]
