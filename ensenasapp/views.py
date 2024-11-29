from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from lessons.utils import inscribir_usuario

def start_view(request):
    return render(request, 'start.html')

def home_view(request):
    return render(request, 'home.html')

def lesson_view(request):
    return render(request, 'lesson.html')

@login_required
def profile_view(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'profile.html', {'user': user})

@login_required
def lessons_view(request):
    return render(request, 'lessons.html')

def lesson_2(request):
    return render(request, 'lesson_2.html')

def lesson_3(request):
    return render(request, 'lesson_3.html')

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
                messages.success(request, 'Registrado con éxito. Por favor, inicia sesión.')
                inscribir_usuario(user)

                return redirect('login')  # Redirige a la página de inicio de sesión
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
            return redirect('home')  # Redirige a la página "home"
        else:
            messages.error(request, 'Datos incorrectos.')
    return render(request, 'login.html')