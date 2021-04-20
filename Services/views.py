from django.shortcuts import render
from core import utill
from django.shortcuts import render
from RADIUS.models import User

def ssh(request):
    print(request)
    today = utill.getStatus("sshd")
    return render(request, "ssh.html", {"Status" : today})