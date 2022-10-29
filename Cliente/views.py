from django.shortcuts import render

def index(request):
    request.session['carrito'] = []
    return render(request, 'Cliente/index.html')

def iniciarSesion(request):
    return render(request, 'Cliente/iniciarSesion.html')
