from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def news(request):
    return render(request, 'news.html')
