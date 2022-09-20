from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm

from django.contrib.auth.models import User

def home(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
