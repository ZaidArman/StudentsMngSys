from django.http import HttpResponse
from django.shortcuts import render

def SignIn(request):
    return render(request, 'index.html')

def SignUp(request):
    return render(request, 'SignUp.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

