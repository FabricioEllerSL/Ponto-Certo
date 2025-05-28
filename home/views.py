from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    Render the home page.
    """

    today = datetime.now().strftime('%d/%m/%Y')
    context = {
        'today': today,
    }

    return render(request, 'home/index.html', context)

@login_required(login_url='home:user_login')
def navigation(request):
    """
    Render the navigation page.
    """

    today = datetime.now().strftime('%d/%m/%Y')
    context = {
        'today': today,
    }
    
    return render(request, 'home/navigation.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:navigation')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'home/login.html')

def user_logout(request):
    logout(request)
    return redirect('home:user_login') 