from django.shortcuts import render
from core import utill
from django.shortcuts import render
from RADIUS.models import User

def ssh(request):
    print(request)
    status = utill.isActive("sshd")
    port = utill.readConfig("sshd", ["Port"])
    return render(request, "ssh.html", {"isActive" : status,"Port" : port})