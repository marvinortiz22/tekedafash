from django.shortcuts import render
from datetime import date
from calendar import HTMLCalendar
import calendar


def index(request):
    fecha_actual = date.today()
    cal = calendar.LocaleHTMLCalendar(firstweekday=6, locale='es').formatmonth(
        fecha_actual.year, fecha_actual.month)
    calCurrent = cambiarCalendario(
        cal, 'cellpadding="0"', 'cellpadding="6px"')
    calCurrent = cambiarCalendario(
        calCurrent, '>%i<' % fecha_actual.day, 'class="" bgcolor="#​008374" ><font color="#FFFFFF"><b>%i</b></font><' % fecha_actual.day)

    return render(request, 'Administrador/index.html', {"cal": calCurrent})


def gestionarProducto(request):
    return render(request, 'Administrador/gestionarProducto.html')


def gestionarCliente(request):
    return render(request, 'Administrador/gestionarCliente.html')


def gestionarAdministrador(request):
    return render(request, 'Administrador/gestionarAdministrador.html')


def cambiarCalendario(objeto, cambio, cambios):
    objeto = objeto.replace(cambio, cambios)
    return objeto
