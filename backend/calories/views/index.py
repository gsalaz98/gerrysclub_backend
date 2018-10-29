from django.shortcuts import render
from django.template import loader

def index(request):
    if request.user.is_authenticated:
        return render(request, 'auth.html')
    else:
        return render(request, 'index.html')