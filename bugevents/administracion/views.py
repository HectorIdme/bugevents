from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from administracion import *

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin')

        messages.info(request, 'Autenticación fallida.')

    context = {}
    return render(request, 'administracion/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
