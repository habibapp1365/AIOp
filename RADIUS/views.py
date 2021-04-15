from core import interfaces
from django.shortcuts import render
import datetime
from RADIUS.models import User


def index(request):
    print(request)
    today = interfaces.get_if()
    #q = User(user='ali', password='123')
    #q.save()
    return render(request, "index.html", {"today" : today})


def login(request):
    today = datetime.datetime.now().date()
    dayofweek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "login.html", {"today": today, "days_of_week": dayofweek})
