from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def div(request):
    return render(request, 'div.html')
    