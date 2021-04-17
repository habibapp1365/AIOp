from core import interfaces
from django.shortcuts import render
import datetime
from RADIUS.models import User


def index(request):
    print(request)
    today = interfaces.get_if()
    return render(request, "index.html", {"today" : today})
