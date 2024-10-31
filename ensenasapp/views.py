from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def start_view(request):
    return render(request, 'start.html')

def home_view(request):
    return render(request, 'home.html')

def lesson_view(request):
    return render(request, 'lesson.html')

def profile_view(request): 
    return render(request, 'profile.html')

def register_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name', '')  
        lastname = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirmpassword = request.POST.get('confirm_password', '')
        
        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El correo ya está registrado.')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está registrado.')
            else:
                user = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()

                user = authenticate(request, username=username, password=password)
            
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Registrado con éxito.')
                    return redirect('home')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Datos incorrectos.')
    return render(request, 'login.html')