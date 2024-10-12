
from django.shortcuts import render

def start_view(request):
    return render(request, 'start.html')

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

def lesson_view(request):
    return render(request, 'lesson.html')