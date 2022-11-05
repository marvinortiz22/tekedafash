from django.shortcuts import render

def index(request):
    return render(request, 'Administrador/index.html')

def gestionarProducto(request):
    return render(request, 'Administrador/gestionarProducto.html')
