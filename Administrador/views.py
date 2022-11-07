from django.shortcuts import render

def index(request):
    return render(request, 'Administrador/index.html')

def gestionarProducto(request):
    return render(request, 'Administrador/gestionarProducto.html')

def gestionarCliente(request):
    return render(request, 'Administrador/gestionarCliente.html')
    
def gestionarAdministrador(request):
    return render(request, 'Administrador/gestionarAdministrador.html')

