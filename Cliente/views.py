from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from Cliente.decorators import *

def index(request):
    request.session['carrito'] = []
    return render(request, 'Cliente/index.html')

@usuarioAutenticado
def iniciarSesion(request):
    if request.method == 'POST':
            nombreUsuario = request.POST.get('usuario')
            contraseña = request.POST.get('contra')
            usuario = authenticate(request, username = nombreUsuario, password = contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('/')
            else:
                messages.error(request, "¡Usuario o contraseña incorrectas!")
                return render(request,'Cliente/iniciarSesion.html' )
    return render(request, 'Cliente/iniciarSesion.html')

@login_required(login_url='iniciarSesion')
def cerrarSesion(request):
    logout(request)
    return redirect('iniciarSesion')
