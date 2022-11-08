from django.shortcuts import render
from datetime import date
from calendar import HTMLCalendar


def index(request):
    fecha_actual = date.today()
    cal = HTMLCalendar().formatmonth(fecha_actual.year, fecha_actual.month)
    return render(request, 'Administrador/index.html', {"cal": cal})


def gestionarProducto(request):
    return render(request, 'Administrador/gestionarProducto.html')

def gestionarCliente(request):
    return render(request, 'Administrador/gestionarCliente.html')
    
def gestionarAdministrador(request):
    return render(request, 'Administrador/gestionarAdministrador.html')

